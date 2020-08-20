from django.urls import path
from django_celery.api.celery_task_results import views


app_name = "api"

urlpatterns = [
    path("", view=views.get_task_results, name="tasks"),
]
