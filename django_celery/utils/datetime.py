import pytz
import datetime
from django.conf import settings


get_current_time = lambda : datetime.datetime.now(pytz.timezone(settings.TIME_ZONE)).strftime(settings.CUSTOM_DATETIME_FORMAT)

convert_date_time = lambda datetime_obj: datetime_obj.strftime(settings.CUSTOM_DATETIME_FORMAT)
