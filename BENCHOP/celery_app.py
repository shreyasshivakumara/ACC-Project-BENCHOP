from celery import Celery 
#broker_url = 'amqp://group4:password@localhost:5672/group4vhost'
broker_url = 'amqp://group4:password@192.168.2.146:5672/group4vhost'
celery_app = Celery('tasks', backend='rpc://', broker=broker_url)