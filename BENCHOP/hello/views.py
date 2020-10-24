from django.shortcuts import render
from hello import tasks
from django.http import JsonResponse
from django.http import HttpResponse
#import matlab.engine
from hello import tasks
from oct2py import Oct2Py
import linecache
# Create your views here.
'''
def index(request):
	return render(request, 'index.html')
'''

def index(request):
    return render(request, 'index.html')

def pa1(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        #print(methods, para_S, para_T, para_K, para_r, para_sig)
        #para_S = list(para_S)
        list_para_S = para_S.split(",")     # str to list
        #array_S = []

        #for ele in list_para_S:
            #array_S.append(float(ele))

        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #print(para)
        prob = 'p_a1'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 a) 1'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'celeryresult.txt', 3)
        
    return render(request, 'pa1.html', log_content)


def pb1(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        #print(methods, para_S, para_T, para_K, para_r, para_sig)
        #para_S = list(para_S)
        list_para_S = para_S.split(",")     # str to list
        #array_S = []

        #for ele in list_para_S:
            #array_S.append(float(ele))

        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #para = [list_para_S, para_K, para_T, para_r, para_sig]      #parameter list
        #print(para)
        prob = 'p_b1'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 b) 1'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'result.txt', 3)

    return render(request, 'pb1.html', log_content)



def pc1(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        
        list_para_S = para_S.split(",")     # str to list
        
        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #para = [list_para_S, para_K, para_T, para_r, para_sig]      #parameter list
        #print(para)
        prob = 'p_c1'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 c) 1'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'result.txt', 3)

    return render(request, 'pc1.html', log_content)


def pa2(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        
        list_para_S = para_S.split(",")     # str to list
        
        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #para = [list_para_S, para_K, para_T, para_r, para_sig]      #parameter list
        #print(para)
        prob = 'p_a2'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 a) 2'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'result.txt', 3)

    return render(request, 'pa2.html', log_content)

def pb2(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        
        list_para_S = para_S.split(",")     # str to list
        
        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #para = [list_para_S, para_K, para_T, para_r, para_sig]      #parameter list
        #print(para)
        prob = 'p_b2'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 b) 2'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'result.txt', 3)

    return render(request, 'pb2.html', log_content)


def pc2(request):
    #engine = matlab.engine.start_matlab()
    oc = Oct2Py()
    time_relerr = []
    log_content = {}
    if request.method == 'POST':
        methods = request.POST.get('method')
        para_S = request.POST.get('S')
        para_T = request.POST.get('T')
        para_K = request.POST.get('K')
        para_r = request.POST.get('r')
        para_sig = request.POST.get('sig')
        
        list_para_S = para_S.split(",")     # str to list
        
        para_K = float(para_K)
        para_T = float(para_T)
        para_r = float(para_r)
        para_sig = float(para_sig)

        #para = [list_para_S, para_K, para_T, para_r, para_sig]      #parameter list
        #print(para)
        prob = 'p_c2'   # problem
        #time_relerr = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig, nargout=2)
        time_relerr = tasks.singlemethodwith_para.delay(prob, methods, list_para_S, para_K, para_T, para_r, para_sig) #call celery
        print(list_para_S, para_K, para_T, para_r, para_sig)
        print(type(list_para_S))

        log_content['problem'] = 'Problem 1 c) 2'
        log_content['methods'] = methods
        log_content['time_and_relerr'] = time_relerr #linecache.getline(r'result.txt', 3)

    return render(request, 'pc2.html', log_content)


