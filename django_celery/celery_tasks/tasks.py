import time
from random import randint

from config import celery_app


@celery_app.task()
def add(a=1, b=1):
    time.sleep(randint(1, 10))
    return a + b


@celery_app.task()
def sub(a=1, b=1):
    time.sleep(randint(1, 10))
    return a - b


@celery_app.task()
def mul(a=1, b=1):
    time.sleep(randint(1, 10))
    return a * b


@celery_app.task()
def div(a=1, b=1):
    time.sleep(randint(1, 10))
    return a / b


@celery_app.task()
def sleep(n):
    time.sleep(n)
    return n
