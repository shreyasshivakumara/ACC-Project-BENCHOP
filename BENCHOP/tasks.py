from oct2py import Oct2Py
from celery_app import celery_app


@celery_app.task
def singleMethod(problem, method):	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/ACC-Project-BENCHOP/BENCHOP/')
	time, relerr = oc.feval('singleMethod', problem, method, nout=2) #use MATLAB files with oct2py
	return  [time, relerr]