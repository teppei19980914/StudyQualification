from datetime import datetime, time
from zoneinfo import ZoneInfo

print("timeModule.py")
print()
print("Time Module")
print("-----------------------------------")
timemodule = time(14, 30, 45)
print("time = time(14, 30, 45)")
print(f"Time: {timemodule}")  # Output: 14:30:45
print(f"Type of time: {type(timemodule)}")  # Output: <class 'datetime.time'>
print("-----------------------------------")
print()
print("ISO Format")
print("-----------------------------------")
isoformatstr = timemodule.isoformat()
print("isoformatstr = timemodule.isoformat()")
print(f"ISO Format: {isoformatstr}")   # Output: 14:30:45
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("ISO Format timespec='hours'")
print("-----------------------------------")
isoformatstr = timemodule.isoformat(timespec='hours')
print("isoformatstr = timemodule.isoformat(timespec='hours')")
print(f"ISO Format: {isoformatstr}")   # Output: 14
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("ISO Format timespec='microseconds'")
print("-----------------------------------")
isoformatstr = timemodule.isoformat(timespec='microseconds')
print("isoformatstr = timemodule.isoformat(timespec='microseconds')")
print(f"ISO Format: {isoformatstr}")   # Output: 14:30:45.000000
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("ISO Format timespec='auto'")
print("-----------------------------------")
isoformatstr = timemodule.isoformat(timespec='auto')
print("isoformatstr = timemodule.isoformat(timespec='auto')")
print(f"ISO Format: {isoformatstr}")   # Output: 14:30:45.000000
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("From ISO Format")
print("-----------------------------------")
fromisoformattime = time.fromisoformat(datetime.now().time().isoformat())
print("isoformattime = time.fromisoformat(datetime.now().time().isoformat())")
print(f"From ISO Format: {fromisoformattime}")  # Output: 14:30:45
print(f"Type of ISO format time: {type(fromisoformattime)}")
print("-----------------------------------")
print()
print("strftime")
print("-----------------------------------")
strftime = timemodule.strftime("%H:%M:%S") # Format: Hour:Minute:Second (e.g., 14:30:45)
print("strftime = timemodule.strftime('%H:%M:%S')")
print(f"strftime: {strftime}")  # Output: 14:30:45
print(f"Type of strftime: {type(strftime)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("tzname")
print("-----------------------------------")
tzname = timemodule.tzname()
print("tzname = timetimemodule.tzname()")
print(f"tzname: {tzname}")  # Output: None
print(f"Type of tzname: {type(tzname)}")  # Output: <class 'NoneType'>
print("-----------------------------------")
print()
print("zoneinfo")
print("-----------------------------------")
zoneinfo = time(14, 30, 45, tzinfo=ZoneInfo("Asia/Tokyo"))
print("zoneinfo = time(14, 30, 45, tzinfo=ZoneInfo('Asia/Tokyo'))")
print(f"Datetime with timezone: {zoneinfo}")  # Output: 2025-02-14 14:30:45+09:00
print(f"Type of datetime with timezone: {type(zoneinfo)}")  # Output: <class 'datetime.time'>
print(f"Timezone name: {zoneinfo.tzname()}")  # Output: JST
print(f"Type of timezone name: {type(zoneinfo.tzname())}")  # Output: <class 'str'>
print("-----------------------------------")
print()