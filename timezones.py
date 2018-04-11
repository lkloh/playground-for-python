import calendar
import time
from datetime import datetime, timedelta
import pytz

start_time = datetime.utcnow() - timedelta(days=1)
stop_time = datetime.utcnow() - timedelta(hours=5) # Have not stopped in UTC-10:00
hawaii_tz = pytz.timezone('US/Hawaii') # UTC-10:00

def date_to_timestamp(date_tuple, local_tz_name):
  local_timezone = pytz.timezone(local_tz_name)
  local_date_tuple = local_timezone.localize(date_tuple)
  print date_tuple
  print local_date_tuple
  naive_date_tuple = datetime(year=local_date_tuple.year, month=local_date_tuple.month, day=local_date_tuple.day, hour=local_date_tuple.hour, minute=local_date_tuple.minute, second=local_date_tuple.second)
  return calendar.timegm(naive_date_tuple.timetuple())

def utc_offset_in_seconds(timezone_name):
  now = datetime.utcnow()
  tz = pytz.timezone(timezone_name)
  return tz.utcoffset(now).total_seconds()
  
offset = utc_offset_in_seconds('US/Hawaii') 
print offset

 


