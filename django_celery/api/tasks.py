import time
from random import randint

from config import celery_app


@celery_app.task()
def add(a, b):
    time.sleep(randint(3, 10))
    return a + b


@celery_app.task()
def sub(a, b):
    time.sleep(randint(3, 10))
    return a - b


@celery_app.task()
def mul(a, b):
    time.sleep(randint(3, 10))
    return a * b


@celery_app.task()
def div(a, b):
    time.sleep(randint(3, 10))
    return a / b
