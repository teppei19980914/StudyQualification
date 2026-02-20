from datetime import datetime
from zoneinfo import ZoneInfo

print("datetimeModule.py")
print()
print("Datetime Module")
print("-----------------------------------")
datetimemodule = datetime(year=2025, month=2, day=14, hour=14, minute=30, second=45)
print("datetimemodule = datetime(year=2025, month=2, day=14, hour=14, minute=30, second=45)")
print(f"Datetime: {datetimemodule}")  # Output: 2025-02-14 14:30:45
print(f"Type of datetime: {type(datetimemodule)}")  # Output: <class 'datetime.datetime'>
print("-----------------------------------")
print()
print("Datetime Module Now")
print("-----------------------------------")
now = datetime.now()
print("now = datetime.now()")
print(f"Now: {now}")  # Output: Current date and time
print(f"Type of now: {type(now)}")  # Output: <class 'datetime.datetime'>
print("-----------------------------------")
print()
print("ISO Format")
print("-----------------------------------")
isoformatstr = now.isoformat()
print("isoformatstr = datetime.isoformat()")
print(f"ISO Format: {isoformatstr}")   # Output: 2025-02-14T14:30:45
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("From ISO Format")
print("-----------------------------------")
fromisoformatdatetime = datetime.fromisoformat(datetimemodule.isoformat())
print("fromisoformatdatetime = datetime.fromisoformat(datetimemodule.isoformat())")
print(f"From ISO Format: {fromisoformatdatetime}")  # Output: 2025-02-14 14:30:45
print(f"Type of ISO format datetime: {type(fromisoformatdatetime)}")  # Output: <class 'datetime.datetime'>
print("-----------------------------------")
print()
print("date")
print("-----------------------------------")
datepart = datetimemodule.date()
print("datepart = datetimemodule.date()")
print(f"Date part: {datepart}")  # Output: 2025-02-14
print(f"Type of date part: {type(datepart)}")  # Output: <class 'datetime.date'>
print("-----------------------------------")
print()
print("time")
print("-----------------------------------")
timepart = datetimemodule.time()
print("timepart = datetimemodule.time()")
print(f"Time part: {timepart}")  # Output: 14:30:45
print(f"Type of time part: {type(timepart)}")  # Output: <class 'datetime.time'>
print("-----------------------------------")
print()
print("strftime")
print("-----------------------------------")
strftime = datetimemodule.strftime("%Y-%m-%d %H:%M:%S") # Format: Year-Month-Day Hour:Minute:Second (e.g., 2025-02-14 14:30:45)
print("strftime = datetimemodule.strftime('%Y-%m-%d %H:%M:%S')")
print(f"strftime: {strftime}")  # Output: 2025-02-14 14:30:45
print(f"Type of strftime: {type(strftime)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("strptime")
print("-----------------------------------")
strptime = datetime.strptime("2025-02-14 14:30:45", "%Y-%m-%d %H:%M:%S")
print("strptime = datetime.strptime('2025-02-14 14:30:45', '%Y-%m-%d %H:%M:%S')")
print(f"strptime: {strptime}")  # Output: 2025-02-14 14:30:45
print(f"Type of strptime: {type(strptime)}")  # Output: <class 'datetime.datetime'>
print("-----------------------------------")
print()
print("tzname")
print("-----------------------------------")
tzname = datetimemodule.tzname()
print("tzname = datetimemodule.tzname()")
print(f"tzname: {tzname}")  # Output: None (if no timezone is set)
print(f"Type of tzname: {type(tzname)}")  # Output: <class 'NoneType'>
print("-----------------------------------")
print()
print("zoneinfo")
print("-----------------------------------")
datetime_with_tz = datetime(year=2025, month=2, day=14, hour=14, minute=30, second=45, tzinfo=ZoneInfo('Asia/Tokyo'))
print("datetime_with_tz = datetime(year=2025, month=2, day=14, hour=14, minute=30, second=45, tzinfo=ZoneInfo('Asia/Tokyo'))")
print(f"Datetime with timezone: {datetime_with_tz}")  # Output: 2025-02-14 14:30:45+09:00
print(f"Type of datetime with timezone: {type(datetime_with_tz)}")  # Output: <class 'datetime.datetime'>
print(f"Timezone name: {datetime_with_tz.tzname()}")  # Output: JST
print(f"Type of timezone name: {type(datetime_with_tz.tzname())}")  # Output: <class 'str'>
print("-----------------------------------")
print()