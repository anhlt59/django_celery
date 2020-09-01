from django.shortcuts import render
from django_celery.celery_tasks import tasks
from django_celery.celery_tasks.models import Video
from django_celery.celery_tasks.forms import VideoForm


def task2(request):
    template = "pages/task2.html"
    context = {
        "user_statistic": tasks.get_users_count(),
        "covid_statistic": tasks.get_statistic_covid()
    }
    return render(request, template, context)


def task5(request):
    template = "pages/task5.html"

    lastvideo = Video.objects.last()
    videofile = lastvideo.videofile if lastvideo else None

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {
        'videofile': videofile,
        'form': form
    }

    return render(request, template, context)
