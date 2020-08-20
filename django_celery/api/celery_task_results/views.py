from django.http.response import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
import random

from django_celery.api.celery_task_results import serializers
from django_celery.celery_tasks import tasks


@csrf_exempt
def get_task_results(request):
    if request.method == "GET":
        pass
        task_id = request.GET.get("task_id")
        task_result = AsyncResult(task_id)
        serializer = serializers.TaskResultSerializer(task_result)
    elif request.method == "POST":
        sleep_time = request.POST.get("sleep_time", random.randint(1, 10))
        task = tasks.sleep.delay(sleep_time)
        serializer = serializers.TaskResultSerializer(task)

    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)



