import time
import requests
import logging
import random
from bs4 import BeautifulSoup
from django.core.cache import cache
from django.contrib.auth import get_user_model
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from config import celery_app
from django_celery.utils import datetime


User = get_user_model()


@celery_app.task()
def sleep(n):
    if n > 30:
        raise Exception("sleep time expired")
    time.sleep(n)
    return n


@celery_app.task()
def error_handler(err=None):
    return err


@celery_app.task()
def add(a, b):
    time.sleep(random.randint(1, 3))
    return a + b


@celery_app.task()
def sub(a, b):
    time.sleep(random.randint(1, 3))
    return a - b


def get_users_count():
    # time.sleep(2)
    current_time = datetime.get_current_time()
    total = User.objects.count()
    superuser = User.objects.filter(is_superuser=True).count()
    staffuser = User.objects.filter(is_staff=True).count()


    return {
        "total": total,
        "superuser": superuser,
        "staffuser": staffuser,
        "update_time": current_time,
    }


def get_statistic_covid():
    # time.sleep(2)
    current_time = datetime.get_current_time()
    url = "https://www.worldometers.info/coronavirus/country/viet-nam/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        total, deaths, recovered = [i.text.strip() for i in soup.select('.maincounter-number')]
        data = {
            "total": total,
            "deaths": deaths,
            "recovered": recovered,
            "update_time": current_time,
        }
    except ValueError:
        logging.warning("Can't extract response html")
        data = None
    return data


@periodic_task(
    run_every=(crontab(minute='*/5')),
    ignore_result=True
)
def update_users_count():
    if data := get_users_count():
        cache.set('users_count', data)


@periodic_task(
    run_every=(crontab(minute='*/5')),
    ignore_result=True
)
def update_statistic_covid():
    if data := get_statistic_covid():
        cache.set('statistic_covid', data)
