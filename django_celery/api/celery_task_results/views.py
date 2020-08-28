import random
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from celery.result import AsyncResult

from django_celery.api.celery_task_results import serializers
from django_celery.celery_tasks import tasks
from config import celery_app
from django_celery.utils import datetime


@csrf_exempt
def get_celery_task_results(request):
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
        task = tasks.sleep.apply_async((sleep_time,), expires=30)
        data = serializers.TaskResultSerializer(task).data
        status = HTTP_200_OK
    return JsonResponse(data, safe=False, status=status)


@csrf_exempt
def get_task_results(request):
    if request.method == "POST":
        sleep_time = int(request.POST.get("sleep_time", random.randint(1, 10)))
        try:
            result = tasks.sleep(sleep_time)
        except:
            result = None
        data = {
            "task_id": "",
            "status": "SUCCESS" if result else "FAIL",
            "result": result,
            "traceback": "",
            "date_done": datetime.get_current_time()
        }
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


@csrf_exempt
def cancel_task(request):
    if task_id := request.GET.get("task_id"):
        celery_app.control.revoke(task_id)
        data = {"status": True}
    else:
        data = {"status": False}
    return JsonResponse(data, safe=False, status=HTTP_200_OK)


############

# # Callback and ErrorBack
# (...).apply_async(link=[add.s(3), add.s(4)], link_error=error_handler.s())
# add.s(1, 2).on_error(error_handler.s())
#
#
# # terminate task is running
# app.task.control.terminate(task_id)
# app.task.control.revoke(task_id, terminate=True)
