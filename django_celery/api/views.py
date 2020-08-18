from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from celery.result import AsyncResult
from django_celery.api import serializers


@csrf_exempt
def get_result(request, task_id):
    task_result = AsyncResult(task_id)
    serializer = serializers.TaskResultSerializer(task_result)
    return JsonResponse(serializer.data)


@csrf_exempt
def get_bulk_result(request):
    task_ids = request.GET.get("task_ids", [])
    task_results = [AsyncResult(task_id) for task_id in task_ids]

    data = serializers.TaskResultSerializer(task_results, many=True).data
    return JsonResponse(data, safe=False, status=200)
