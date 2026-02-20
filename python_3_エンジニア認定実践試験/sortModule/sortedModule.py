from colorama import init, Fore
from ast import List
from typing import Union

init(autoreset=True)

print()
print("sortedModule.py")
print(Fore.RED + "sorted関数は、元のリストを変更せずに新しいソートされたリストを返します。")
print()
numbers: List[int] = [5, 2, 9, 1, 5, 6]
print("numbers: List[int] = [5, 2, 9, 1, 5, 6]")
print("Sorted Method Used List Of Integers")
print("-----------------------------------")
sorted_numbers = sorted(numbers)
print("sorted_numbers = sorted(numbers)")
print(f"Sorted Numbers: {sorted_numbers}")  # Output: [1, 2, 5, 5, 6, 9]
print(f"Original Numbers: {numbers}")  # Output: [5, 2, 9, 1, 5, 6]
print(f"Type of sorted_numbers: {type(sorted_numbers)}")  # Output: <class 'list'>
print("-----------------------------------")
print()
print("Sorted Method Used List Of Integers With Reverse=False")
print("-----------------------------------")
sorted_numbers_reverse_false = sorted(numbers, reverse=False)
print("sorted_numbers_reverse_false = sorted(numbers, reverse=False)")
print(f"Sorted Numbers: {sorted_numbers_reverse_false}")  # Output: [1, 2, 5, 5, 6, 9]
print(f"sorted_numbers == sorted_numbers_reverse_false: {sorted_numbers == sorted_numbers_reverse_false}")  # Output: True
print(f"Type of sorted_numbers_reverse_false: {type(sorted_numbers_reverse_false)}")  # Output: <class 'list'>
print("-----------------------------------")
print()
print("Sorted Method Used List Of Integers With Reverse=True")
print("-----------------------------------")
sorted_numbers_reverse_true = sorted(numbers, reverse=True)
print("sorted_numbers_reverse_true = sorted(numbers, reverse=True)")
print(f"Sorted Numbers: {sorted_numbers_reverse_true}")  # Output: [9, 6, 5, 5, 2, 1]
print(f"sorted_numbers == sorted_numbers_reverse_true: {sorted_numbers == sorted_numbers_reverse_true}")  # Output: False
print(f"Type of sorted_numbers_reverse_true: {type(sorted_numbers_reverse_true)}")  # Output: <class 'list'>
print("-----------------------------------")
print()

strings: List[str] = ["banana", "apple", "cherry"]
print("strings: List[str] = [\"banana\", \"apple\", \"cherry\"]")
print("Sorted Method Used List Of Strings")
print("-----------------------------------")
sorted_strings = sorted(strings)
print("sorted_strings = sorted(strings)")
print(f"Sorted Strings: {sorted_strings}")  # Output: ['apple', 'banana', 'cherry']
print(f"Original Strings: {strings}")  # Output: ['banana', 'apple', 'cherry']
print(f"Type of sorted_strings: {type(sorted_strings)}")  # Output: <class 'list'>
print("-----------------------------------")
print()
print("Sorted Method Used List Of strings With Reverse=False")
print("-----------------------------------")
sorted_strings_reverse_false = sorted(strings, reverse=False)
print("sorted_strings_reverse_false = sorted(strings, reverse=False)")
print(f"Sorted Strings: {sorted_strings_reverse_false}")  # Output: ['apple', 'banana', 'cherry']
print(f"sorted_strings == sorted_strings_reverse_false: {sorted_strings == sorted_strings_reverse_false}")  # Output: True
print(f"Type of sorted_strings_reverse_false: {type(sorted_strings_reverse_false)}")  # Output: <class 'list'>
print("-----------------------------------")
print()
print("Sorted Method Used List Of strings With Reverse=True")
print("-----------------------------------")
sorted_strings_reverse_true = sorted(strings, reverse=True)
print("sorted_strings_reverse_true = sorted(strings, reverse=True)")
print(f"Sorted Strings: {sorted_strings_reverse_true}")  # Output: ['cherry', 'banana', 'apple']
print(f"sorted_strings == sorted_strings_reverse_true: {sorted_strings == sorted_strings_reverse_true}")  # Output: False
print(f"Type of sorted_strings_reverse_true: {type(sorted_strings_reverse_true)}")  # Output: <class 'list'>
print("-----------------------------------")
print()

stringintegers: List[Union[str, int]] = ["banana", "apple", "cherry", 5, 2, 9, 1, 5, 6]
print("strings: List[Union[str, int]] = [\"banana\", \"apple\", \"cherry\", 5, 2, 9, 1, 5, 6]")
print("Sorted Method Used List Of Strings And Integers")
print("-----------------------------------")
try:
    print("sorted_stringintegers = sorted(stringintegers)")
    sorted_stringintegers = sorted(stringintegers)
except TypeError as e:
    print(f"TypeError: {e}", "Cannot compare different types.")
print("-----------------------------------")
print()

tuples: tuple = (5, 2, 9, 1, 5, 6)
print("tuples: tuple = (5, 2, 9, 1, 5, 6)")
print("Sorted Method Used Tuple Of Integers")
print("-----------------------------------")
sorted_tuples = sorted(tuples)
print("sorted_tuples = sorted(tuples)")
print(f"Sorted Tuple: {sorted_tuples}")  # Output: [1, 2, 5, 5, 6, 9]
print(f"Type of sorted_tuples: {type(sorted_tuples)}")  # Output: <class 'list'>
print("-----------------------------------")
print()

dictionary: dict = {"banana": 3, "apple": 2, "cherry": 5}
print("dictionary: dict = {\"banana\": 3, \"apple\": 2, \"cherry\": 5}")
print("Sorted Method Used Dictionary")
print("-----------------------------------")
sorted_dictionary = sorted(dictionary)
print("sorted_dictionary = sorted(dictionary)")
print(f"Sorted Dictionary Keys: {sorted_dictionary}")  # Output: ['apple', 'banana', 'cherry']
print(f"Type of sorted_dictionary: {type(sorted_dictionary)}")  # Output: <class 'list'>
print("-----------------------------------")
print()

set_of_numbers: set = {5, 2, 9, 1, 5, 6}
print("set_of_numbers: set = {5, 2, 9, 1, 5, 6}")
print("Sorted Method Used Set Of Integers")
print("-----------------------------------")
sorted_set_of_numbers = sorted(set_of_numbers)
print("sorted_set_of_numbers = sorted(set_of_numbers)")
print(f"Sorted Set Of Numbers: {sorted_set_of_numbers}")  # Output: [1, 2, 5, 6, 9]
print(f"Type of sorted_set_of_numbers: {type(sorted_set_of_numbers)}")  # Output: <class 'list'>
print("-----------------------------------")
print()

string: str = "banana"
print("string: str = \"banana\"")
print("Sorted Method Used String")
print("-----------------------------------")
sorted_string = sorted(string)
print("sorted_string = sorted(string)")
print(f"Sorted String: {sorted_string}")  # Output: ['a', 'a', 'b', 'n', 'n']
print(f"Type of sorted_string: {type(sorted_string)}")  # Output: <class 'list'>
print("-----------------------------------")
print()