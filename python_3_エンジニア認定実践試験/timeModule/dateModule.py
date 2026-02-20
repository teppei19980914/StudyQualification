from datetime import date

print("dateModule.py")
print()
print("Date Module")
print("-----------------------------------")
date = date(2025, 2, 14)
print("date = date(2025, 2, 14)")
print(f"Date: {date}")  # Output: 2025-02-14
print(f"Type of date: {type(date)}")  # Output: <class 'datetime.date'>
print("-----------------------------------")
print()
print("Date Module")
print("-----------------------------------")
print('f"Year: {date.year}, Month: {date.month}, Day: {date.day}"')
print(f"Year: {date.year}, Month: {date.month}, Day: {date.day}")   # Output: Year: 2025, Month: 2, Day: 14
print(f"Type of year: {type(date.year)}, Type of month: {type(date.month)}, Type of day: {type(date.day)}")    # Output: <class 'int'>
print("-----------------------------------")
print()
print("Today's Date")  # Output: 0001-01-01
print("-----------------------------------")
today = date.today()  # Use date.today() to get the current date
print("today = date.today()")
print(f"Date: {today}")  # Output: 2025-02-14
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")   # Output: Year: 2025, Month: 2, Day: 14
print(f"Type of date: {type(today)}")  # Output: <class 'datetime.date'>
print("-----------------------------------")
print()
print("Weekday")  # Output: 0001-01-01
print("-----------------------------------")
weelday = today.weekday()
print("weelday = date.weekday()")
print(f"Weekday: {weelday}")     # Output: 4 (Friday, where Monday is 0 and Sunday is 6)
print(f"Type of weekday: {type(weelday)}")  # Output: <class 'int'>
print("-----------------------------------")
print()
print("ISO Weekday")  # Output: 0001-01-01
print("-----------------------------------")
weelday = date.isoweekday()
print("weelday = date.isoweekday()")
print(f"Weekday: {weelday}")     # Output: 4 (Friday, where Monday is 0 and Sunday is 6)
print(f"Type of weekday: {type(weelday)}")  # Output: <class 'int'>
print("-----------------------------------")
print()
print("ISO Format")
print("-----------------------------------")
isoformatstr = date.isoformat()
print("isoformatstr = date.isoformat()")
print(f"ISO Format: {isoformatstr}")   # Output: 2025-02-14
print(f"Type of ISO format string: {type(isoformatstr)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("From ISO Format")
print("-----------------------------------")
fromisoformatdate = date.fromisoformat("2025-02-14")
print("fromisoformatdate = date.fromisoformat('2025-02-14')")
print(f"From ISO Format: {fromisoformatdate}")  # Output: 2025-02-14
print(f"Type of ISO format date: {type(fromisoformatdate)}")  # Output: <class 'datetime.date'>
print("-----------------------------------")
print()
print("strftime")
print("-----------------------------------")
strftime = date.strftime("%Y/%m/%d") # Format: Year/Month/Day (e.g., 2025/02/14)
print("strftime = date.strftime('%Y/%m/%d')")
print(f"strftime: {strftime}")  # Output: 2025/02/14
print(f"Type of strftime: {type(strftime)}")  # Output: <class 'str'>
print("-----------------------------------")
print()
print("f-strings")
print("-----------------------------------")
print("f'今日は{today:%Y年%m月%d日です。}'")
print(f'今日は{today:%Y年%m月%d日です。}')
print("-----------------------------------")
print()