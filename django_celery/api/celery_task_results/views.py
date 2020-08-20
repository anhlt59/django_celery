import random
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from celery.result import AsyncResult


from django_celery.api.celery_task_results import serializers
from django_celery.celery_tasks import tasks


@csrf_exempt
def get_task_results(request):
    if request.method == "GET":
        if task_id := request.GET.get("task_id", None):
            task_result = AsyncResult(task_id)
            data = serializers.TaskResultSerializer(task_result).data
            status = HTTP_200_OK
        else:
            status = HTTP_400_BAD_REQUEST
            data = None
    elif request.method == "POST":
        sleep_time = int(request.POST.get("sleep_time", random.randint(1, 10)))
        task = tasks.sleep.delay(sleep_time)
        data = serializers.TaskResultSerializer(task).data
        status = HTTP_200_OK
    return JsonResponse(data, safe=False, status=status)


@csrf_exempt
def get_statistic_covid(request):
    data = cache.get('statistic_covid')
    return JsonResponse(data, safe=False, status=HTTP_200_OK)


@csrf_exempt
def get_users_count(request):
    data = cache.get('users_count')
    return JsonResponse(data, safe=False, status=HTTP_200_OK)
