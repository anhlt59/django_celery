from django.urls import path
from django.views.generic import TemplateView
from django_celery.celery_tasks import views

app_name = "celery_tasks"

urlpatterns = [
    path("celery-1", TemplateView.as_view(template_name="pages/task1.html"), name="task1"),
    path("celery-2", views.task2, name="task2"),
    path("celery-3", TemplateView.as_view(template_name="pages/task3.html"), name="task3"),
    path("celery-4", TemplateView.as_view(template_name="pages/task4.html"), name="task4"),
    path("celery-5", views.task5, name="task5"),
]
