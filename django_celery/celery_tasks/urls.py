from django.urls import path
from django_celery.celery_tasks import views


app_name = "api"

urlpatterns = [
    path("<slug:task_id>", view=views.get_result, name="task"),
    path("", view=views.get_task_results, name="tasks"),
    path("create", view=views.create_task, name="create"),
    # path("run_task", view=views.get_bulk_result, name="tasks"),
]
