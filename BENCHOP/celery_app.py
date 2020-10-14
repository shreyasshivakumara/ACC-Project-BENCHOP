from celery import Celery 
broker_url = 'amqp://group4:password@localhost:5672/group4vhost'

celery_app = Celery('tasks', backend='rpc://', broker=broker_url)