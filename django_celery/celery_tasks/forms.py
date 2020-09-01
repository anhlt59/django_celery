from django import forms
from django_celery.celery_tasks.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ("name", "videofile")
