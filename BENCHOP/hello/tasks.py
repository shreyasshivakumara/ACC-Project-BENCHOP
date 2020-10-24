'''
from __future__ import absolute_import
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y
'''

from oct2py import Oct2Py
#from celery_app import celery_app
from celery import shared_task
#import matlab.engine
'''
@celery_app.task
def singleMethod(problem, method):	
	oc = Oct2Py()
	oc.chdir('/home/ubuntu/ACC-Project-BENCHOP/BENCHOP/')
	time, relerr = oc.feval('singleMethod', problem, method, nout=2) #use MATLAB files with oct2py
	return  [time, relerr]
'''
@shared_task
def singlemethodwith_para(prob, methods, list_para_S, para_K, para_T, para_r, para_sig):
	oc = Oct2Py()
	[time, relerr] = oc.singleMethodWithParams(prob, methods, list_para_S, para_K, para_T, para_r, para_sig,nout=2)

	return time, relerr
