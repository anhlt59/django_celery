from django.shortcuts import render
from django_celery.celery_tasks import tasks


def task2(request):
    template = "pages/task2.html"
    context = {
        "user_statistic": tasks.get_users_count(),
        "covid_statistic": tasks.get_statistic_covid()
    }
    return render(request, template, context)
