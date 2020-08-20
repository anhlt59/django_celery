from django.urls import path
from django_celery.api.celery_task_results import views


app_name = "api"

urlpatterns = [
    path("", view=views.get_task_results, name="tasks"),
    path("statistic-covid", view=views.get_statistic_covid, name="get_statistic_covid"),
    path("users-count", view=views.get_users_count, name="users_count"),
]
