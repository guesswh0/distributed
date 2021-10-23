import os

from celery import Celery

celery = Celery(__name__, broker=os.environ['BROKER_URL'])


@celery.task
def add(a, b):
    return a + b


if __name__ == '__main__':
    celery.start()
