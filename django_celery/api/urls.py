from django.urls import path
from django_celery.api import views


app_name = "api"

urlpatterns = [
    path("task/<slug:task_id>", view=views.get_result, name="task"),
    path("tasks", view=views.get_bulk_result, name="tasks"),
]
