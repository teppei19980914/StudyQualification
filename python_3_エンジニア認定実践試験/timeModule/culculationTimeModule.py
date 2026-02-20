from colorama import init, Fore
from datetime import date, time, datetime
from zoneinfo import ZoneInfo

init(autoreset=True)

print("culculationTimeModule.py")
print()
print("Time Module Naive Calculation")
print("-----------------------------------")
print(Fore.RED + "timeオブジェクトは、日付やタイムゾーンの情報を持たないため、単純な引き算はできません。")
try:
    print("naivetime1 = time(10, 30, 45)")
    naivetime1 = time(10, 30, 45)
    print(f"Naive Time 1: {naivetime1}")  # Output: 10:30:45
    print(f"timezone info: {naivetime1.tzinfo}")  # Output: None
    print("naivetime2 = time(2, 30, 45)")
    naivetime2 = time(2, 30, 45)
    print(f"Naive Time 2: {naivetime2}")  # Output: 02:30:45
    print(f"timezone info: {naivetime2.tzinfo}")  # Output: None
    print("resulttime = naivetime1 - naivetime2")
    resulttime = naivetime1 - naivetime2
    print(f"Result Time: {resulttime}")  # Output: 08:00:00
except TypeError as e:
    print(f"Error: {e} - Time objects do not support subtraction directly.")
print("-----------------------------------")
print()
print("Date Module Naive Calculation")
print("-----------------------------------")
naivedate1 = date(2025, 2, 14)
print("naivedate1 = date(2025, 2, 14)")
print(f"Naive Date 1: {naivedate1}")  # Output: 2025-02-14
naivedate2 = date(2025, 2, 7)
print("naivedate2 = date(2025, 2, 7)")
print(f"Naive Date 2: {naivedate2}")  # Output: 2025-02-07
resultdate = naivedate1 - naivedate2
print("resultdate = naivedate1 - naivedate2")
print(f"Result Date: {resultdate}")  # Output: 7 days, 0:00:00
print("-----------------------------------")
print()
print("Datetime Module Naive Calculation")
print("-----------------------------------")
naivedatetime1 = datetime(2025, 2, 14, 10, 30, 45)
print("naivedatetime1 = datetime(2025, 2, 14, 10, 30, 45)")
print(f"Naive Datetime 1: {naivedatetime1}")  # Output: 2025-02-14 10:30:45
naivedatetime2 = datetime(2025, 2, 7, 2, 15, 45)
print("naivedatetime2 = datetime(2025, 2, 7, 2, 15, 45)")
print(f"Naive Datetime 2: {naivedatetime2}")  # Output: 2025-02-07 02:15:45
resultdatetime = naivedatetime1 - naivedatetime2
print("resultdatetime = naivedatetime1 - naivedatetime2")
print(f"Result Datetime: {resultdatetime}")  # Output: 7 days, 8:15:00
print("-----------------------------------")
print()
print("Time Module Aware Calculation")
print("-----------------------------------")
print(Fore.RED + "timeオブジェクトは、日付やタイムゾーンの情報を持たないため、単純な引き算はできません。")
try:
    awaretime1 = time(10, 30, 45, tzinfo=ZoneInfo("Asia/Tokyo"))
    print("awaretime1 = time(10, 30, 45, tzinfo=ZoneInfo('Asia/Tokyo'))")
    print(f"Aware Time 1: {awaretime1}")  # Output: 10:30:45+09:00
    print(f"timezone info: {awaretime1.tzinfo}")  # Output: Asia/Tokyo
    awaretime2 = time(2, 30, 45, tzinfo=ZoneInfo("Asia/Tokyo"))
    print("awaretime2 = time(2, 30, 45, tzinfo=ZoneInfo('Asia/Tokyo'))")
    print(f"Aware Time 2: {awaretime2}")  # Output: 02:30:45+09:00
    print(f"timezone info: {awaretime2.tzinfo}")  # Output: Asia/Tokyo
    print("resultawaretime = awaretime1 - awaretime2")
    resultawaretime = awaretime1 - awaretime2
    print(f"Result Aware Time: {resultawaretime}")  # Output: 08:00:00
except TypeError as e:
    print(f"Error: {e} - Time objects do not support subtraction directly.")
print("-----------------------------------")
print()
print("Datetime Module Aware Calculation")
print("-----------------------------------")
awaredatetime1 = datetime(2025, 2, 14, 10, 30, 45, tzinfo=ZoneInfo("Asia/Tokyo"))
print("awaredatetime1 = datetime(2025, 2, 14, 10, 30, 45, tzinfo=ZoneInfo('Asia/Tokyo'))")
print(f"Aware Datetime 1: {awaredatetime1}")  # Output: 2025-02-14 10:30:45+09:00
awaredatetime2 = datetime(2025, 2, 7, 2, 15, 45, tzinfo=ZoneInfo("Asia/Tokyo"))
print("awaredatetime2 = datetime(2025, 2, 7, 2, 15, 45, tzinfo=ZoneInfo('Asia/Tokyo'))")
print(f"Aware Datetime 2: {awaredatetime2}")  # Output: 2025-02-07 02:15:45+09:00
resultawaredatetime = awaredatetime1 - awaredatetime2
print("resultawaredatetime = awaredatetime1 - awaredatetime2")
print(f"Result Aware Datetime: {resultawaredatetime}")  # Output: 7 days, 8:15:00
print("-----------------------------------")
print()
print("Aware vs Naive Datetime Calculation")
print("-----------------------------------")
print(Fore.RED + "awareなdatetimeオブジェクトとnaiveなdatetimeオブジェクトを混ぜて計算することはできません。")
try:
    print("resultmixeddatetime = awaredatetime1 - naivedatetime2")
    resultmixeddatetime = awaredatetime1 - naivedatetime2
    print(f"Result Mixed Datetime: {resultmixeddatetime}")  # This line should not execute
except TypeError as e:
    print(f"Error: {e} - Cannot mix aware and naive datetime objects.")