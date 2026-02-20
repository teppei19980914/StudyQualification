from colorama import init, Fore
from ast import List
import copy
from typing import Union

init(autoreset=True)

print()
print("sortModule.py")
print(Fore.RED + "sortメソッドは、リストを直接変更するため、元のリストが変更されます。")
print()
numbers: List[int] = [5, 2, 9, 1, 5, 6]
print("numbers: List[int] = [5, 2, 9, 1, 5, 6]")
try:
    print("Sort Method Used List Of Integers")
    print("-----------------------------------")
    sortNumbers = copy.copy(numbers)
    sortNumbers.sort()
    print("sort_numbers = sort(numbers)")
    print(f"Sort Numbers: {sortNumbers}")  # Output: [1, 2, 5, 5, 6, 9]
    print(f"Original Numbers: {numbers}")  # Output: [5, 2, 9, 1, 5, 6]
    print(f"Type of sort_numbers: {type(sortNumbers)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()
try:
    print("Sort Method Used List Of Integers With Reverse=False")
    print("-----------------------------------")
    sortNumbers = copy.copy(numbers)
    sortNumbers.sort(reverse=False)
    print("sort_numbers_reverse_false = sort(numbers, reverse=False)")
    print(f"Sort Numbers: {sortNumbers}")  # Output: [1, 2, 5, 5, 6, 9]
    print(f"Type of sort_numbers_reverse_false: {type(sortNumbers)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()
try:
    print("Sort Method Used List Of Integers With Reverse=True")
    print("-----------------------------------")
    sortNumbers = copy.copy(numbers)
    sortNumbers.sort(reverse=True)
    print("sort_numbers_reverse_true = sort(numbers, reverse=True)")
    print(f"Sort Numbers: {sortNumbers}")  # Output: [9, 6, 5, 5, 2, 1]
    print(f"Type of sort_numbers_reverse_true: {type(sortNumbers)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()

strings: List[str] = ["banana", "apple", "cherry"]
print("strings: List[str] = [\"banana\", \"apple\", \"cherry\"]")
try:
    print("Sort Method Used List Of Strings")
    print("-----------------------------------")
    sortstrings = copy.copy(strings)
    sortstrings.sort()
    print("sort_strings = sort(strings)")
    print(f"Sort Strings: {sortstrings}")  # Output: ['apple', 'banana', 'cherry']
    print(f"Type of sort_strings: {type(sortstrings)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()
try:
    print("Sort Method Used List Of strings With Reverse=False")
    print("-----------------------------------")
    sortstrings = copy.copy(strings)
    sortstrings.sort(reverse=False)
    print("sort_strings_reverse_false = sort(strings, reverse=False)")
    print(f"Sort Strings: {sortstrings}")  # Output: ['apple', 'banana', 'cherry']
    print(f"Type of sort_strings_reverse_false: {type(sortstrings)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()
try:
    print("Sort Method Used List Of strings With Reverse=True")
    print("-----------------------------------")
    sortstrings = copy.copy(strings)
    sortstrings.sort(reverse=True)
    print("sort_strings_reverse_true = sort(strings, reverse=True)")
    print(f"Sort Strings: {sortstrings}")  # Output: ['cherry', 'banana', 'apple']
    print(f"Type of sort_strings_reverse_true: {type(sortstrings)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()

stringintegers: List[Union[str, int]] = ["banana", "apple", "cherry", 5, 2, 9, 1, 5, 6]
print("strings: List[Union[str, int]] = [\"banana\", \"apple\", \"cherry\", 5, 2, 9, 1, 5, 6]")
print("Sort Method Used List Of Strings And Integers")
print("-----------------------------------")
try:
    print("sortstringintegers = copy.copy(stringintegers)")
    sortstringintegers = copy.copy(stringintegers)
    print("sort_stringintegers = sort(stringintegers)")
    sort_stringintegers = sortstringintegers.sort(stringintegers)
except TypeError as e:
    print(f"TypeError: {e}", "Cannot compare different types.")
print("-----------------------------------")
print()

tuples: tuple = (5, 2, 9, 1, 5, 6)
print("tuples: tuple = (5, 2, 9, 1, 5, 6)")
try:
    print("Sort Method Used Tuple Of Integers")
    print("-----------------------------------")
    sorttuple = list(tuples)
    sorttuple.sort()
    print("sort_tuples = sort(tuples)")
    print(f"Sort Tuple: {sorttuple}")  # Output: [1, 2, 5, 5, 6, 9]
    print(f"Type of sort_tuples: {type(sorttuple)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()

dictionary: dict = {"banana": 3, "apple": 2, "cherry": 5}
print("dictionary: dict = {\"banana\": 3, \"apple\": 2, \"cherry\": 5}")
try:
    print("Sort Method Used Dictionary")
    print("-----------------------------------")
    sortdictionary = list(dictionary.keys())
    sortdictionary.sort()
    print("sort_dictionary = sort(dictionary)")
    print(f"Sort Dictionary Keys: {sortdictionary}")  # Output: ['apple', 'banana', 'cherry']
    print(f"Type of sort_dictionary: {type(sortdictionary)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()

set_of_numbers: set = {5, 2, 9, 1, 5, 6}
print("set_of_numbers: set = {5, 2, 9, 1, 5, 6}")
try:
    print("Sort Method Used Set Of Integers")
    print("-----------------------------------")
    sort_set_of_numbers = list(set_of_numbers)
    sort_set_of_numbers.sort()
    print("sort_set_of_numbers = sort(set_of_numbers)")
    print(f"Sort Set Of Numbers: {sort_set_of_numbers}")  # Output: [1, 2, 5, 6, 9]
    print(f"Type of sort_set_of_numbers: {type(sort_set_of_numbers)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()

string: str = "banana"
print("string: str = \"banana\"")
try:
    print("Sort Method Used String")
    print("-----------------------------------")
    sort_string = list(string)
    sort_string.sort()
    print("sort_string = sort(string)")
    print(f"Sort String: {sort_string}")  # Output: ['a', 'a', 'b', 'n', 'n']
    print(f"Type of sort_string: {type(sort_string)}")  # Output: <class 'list'>
    print("-----------------------------------")
finally:
    print()