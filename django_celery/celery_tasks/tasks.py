import time
import requests
import logging
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
    time.sleep(n)
    return n


@periodic_task(
    run_every=(crontab(minute='*/5')),
    ignore_result=True
)
def update_statistic_covid():
    current_time = datetime.get_current_time()
    url = "https://www.worldometers.info/coronavirus/country/viet-nam/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    try:
        total, deaths, recovered = [i.text.strip() for i in soup.select('.maincounter-number')]
        data = {
            "total":total,
            "deaths":deaths,
            "recovered":recovered,
            "update_time":current_time,
        }
        cache.set('statistic_covid', data)
    except ValueError:
        logging.warning("Can't extract response html")


@periodic_task(
    run_every=(crontab(minute='*/5')),
    ignore_result=True
)
def update_users_count():
    current_time = datetime.get_current_time()
    users_count = User.objects.count()
    data = {
        "users_count": users_count,
        "current_time": current_time,
    }
    cache.set('users_count', data)
