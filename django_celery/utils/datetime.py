import pytz
import datetime
from django.conf import settings


get_current_time = lambda : datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)).strftime("%B %d, %Y, %I:%M %p")
