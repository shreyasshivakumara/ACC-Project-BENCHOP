from tasks import singleMethod
from celery_app import celery_app
from celery import group
from celery.result import AsyncResult
import time
from flask import Flask, jsonify, render_template, request
import pygal, json
from pygal.style import Style
from pygal.style import CleanStyle, DefaultStyle
start = time.time()

#problems stated in Table.m
ALL_PROBLEMS = ['P1aI', 'P1bI', 'P1cI', 'P1aII']
ALL_METHODS = ['MC','MC-S','QMC-S','MLMC','MLMC-A','FFT','FGL','COS','FD','FD-NU','FD-AD','RBF','RBF-FD','RBF-PUM','RBF-LSML','RBF-AD','RBF-MLT']
#but for testing puroses, only use subset of methods and problems
METHODS = ['COS', 'UniformGrid']
PROBLEMS = ['P1aI', 'P1bI']
#Start benchmarking tasks
ALL_RESULTS = {}
for prob in PROBLEMS:
	ALL_RESULTS[prob] = {}
	for method in METHODS:
		result = singleMethod.delay(prob, method)
		ALL_RESULTS[prob][method] = {'state': 'PENDING', 'id': result.id, 'result': {'time': 0, 'relerr': 0}}

#Use this to update state
def update_results():
	for prob in ALL_RESULTS.keys():
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'PENDING':
				result = AsyncResult(ALL_RESULTS[prob][method]['id'], app=celery_app)
				while result.state != 'SUCCESS':
					time.sleep(1)
				if result.state == 'SUCCESS':
					ALL_RESULTS[prob][method]['state'] = result.state
					ALL_RESULTS[prob][method]['result']['time'] = result.result[0]
					ALL_RESULTS[prob][method]['result']['relerr'] = result.result[1]




#Start the flask app after all tasks are created
flask_app = Flask(__name__)

#Updates global variable with newly finished results and returns everything
@flask_app.route('/benchmark', methods=['GET'])
def obtain_benchmark_results():
	global ALL_RESULTS
	update_results()
	
	time_charts = []
	relerr_charts = []
	print("start rendering..")
	for prob in sorted(ALL_RESULTS.keys()):
		time_chart = pygal.Bar(style=CleanStyle)
		time_chart.title = "Time to solve problem: " + prob
		time_chart.y_title = "Execution time [s]"

		relerr_chart = pygal.Bar(style=DefaultStyle)
		relerr_chart.title = "Relative error for problem: " + prob
		relerr_chart.y_title = "Relative error"

		labels = []
		time_data = []
		relerr_data = []
		for method in ALL_RESULTS[prob].keys():
			if ALL_RESULTS[prob][method]['state'] == 'SUCCESS':
				labels.append(method)
			else:
				labels.append(method + " PENDING")

			time_data.append(ALL_RESULTS[prob][method]['result']['time'])
			relerr_data.append(ALL_RESULTS[prob][method]['result']['relerr'])

		time_chart.x_labels = map(str, labels)
		time_chart.add('Time', time_data)
		time_chart_data = time_chart.render_data_uri()
		time_charts.append(time_chart_data)

		relerr_chart.x_labels = map(str, labels)
		relerr_chart.add('Relerr', relerr_data)
		relerr_chart_data = relerr_chart.render_data_uri()
		relerr_charts.append(relerr_chart_data)
	print("done rendering...")
	return render_template("webui.html", results = ALL_RESULTS, time_charts = time_charts, relerr_charts = relerr_charts)


@flask_app.route('/benchmark/json', methods=['GET'])
def obtain_results_json():
	global ALL_RESULTS
	update_results()
	return jsonify(ALL_RESULTS)

	
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port = 50070, debug=True)
