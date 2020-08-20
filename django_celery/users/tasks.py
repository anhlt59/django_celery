from django.contrib.auth import get_user_model
import time

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    return User.objects.count()
