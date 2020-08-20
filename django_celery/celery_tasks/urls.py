from django.urls import path
from django.views.generic import TemplateView
from django_celery.celery_tasks import views


app_name = "celery_tasks"

urlpatterns = [
    path("1", TemplateView.as_view(template_name="pages/task1.html"), name="task1"),
    path("2", TemplateView.as_view(template_name="pages/task2.html"), name="task2"),
    path("3", TemplateView.as_view(template_name="pages/task3.html"), name="task3"),
]
