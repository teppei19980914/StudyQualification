from datetime import timedelta, datetime, date
import dateModule
import datetimeModule
import timeModule

print("timedeltaModule.py")
print()
print("Timedelta Module")
print("-----------------------------------")
oneweek = timedelta(days=7)
print("oneweek = timedelta(days=7)")
print(f"One week ago: {oneweek}")  # Output: Date one week ago
print(f"Type of one week ago: {type(oneweek)}")  # Output: <class 'datetime.timedelta'>
print("-----------------------------------")
print()
print("One Week Later With Date Module")
print("-----------------------------------")
oneweeklater = dateModule.today - oneweek
print("oneweeklater = dateModule.today + oneweek")
print(f"One week later: {oneweeklater}")  # Output: Date one week later
print(f"Type of one week later: {type(oneweeklater)}")  # Output: <class 'datetime.date'>
print("-----------------------------------")
print()
print("One Week Ago With Datetime Module")
print("-----------------------------------")
oneweekago = datetimeModule.datetimemodule + oneweek
print("oneweekago = datetimeModule.datetimemodule + oneweek")
print(f"One week ago: {oneweekago}")  # Output: Datetime one week ago
print(f"Type of one week ago: {type(oneweekago)}")  # Output: <class 'datetime.datetime'>
print("-----------------------------------")
print()
print("Seven Hours Later With Time Module")
print("-----------------------------------")
sevenhourslater = datetime.combine(date.today(), timeModule.fromisoformattime) - timedelta(hours=7)
print("sevenhourslater = datetime.combine(date.today(), timeModule.fromisoformattime) - timedelta(hours=7)")
print(f"Seven hours later: {sevenhourslater}")  # Output: Time seven hours later
print(f"Type of seven hours later: {type(sevenhourslater)}")  # Output: <class 'datetime.time'>
print("-----------------------------------")
print()