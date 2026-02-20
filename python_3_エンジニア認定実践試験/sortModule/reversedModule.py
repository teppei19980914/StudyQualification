from colorama import init, Fore
from ast import List
from ctypes import Union

init(autoreset=True)

print()
print("reversedModule.py")
print()
numbers: List[int] = [5, 2, 9, 1, 5, 6]
print("numbers: List[int] = [5, 2, 9, 1, 5, 6]")
print("Reversed Method Used List Of Integers")
print("-----------------------------------")
reversed_numbers = reversed(numbers)
print("reversed_numbers = reversed(numbers)")
print(f"Reversed Numbers: {list(reversed_numbers)}")  # Output: [6, 5, 1, 9, 2, 5]
print(f"Original Numbers: {numbers}")  # Output: [5, 2, 9, 1, 5, 6]
print(f"Type of reversed_numbers: {type(reversed_numbers)}")  # Output: <class 'list_reverseiterator'>
print("-----------------------------------")
print()

strings: List[str] = ["banana", "apple", "cherry"]
print("strings: List[str] = [\"banana\", \"apple\", \"cherry\"]")
print("Reversed Method Used List Of Strings")
print("-----------------------------------")
reversed_strings = reversed(strings)
print("reversed_strings = reversed(strings)")
print(f"Reversed Strings: {list(reversed_strings)}")  # Output: ['cherry', 'apple', 'banana']
print(f"Original Strings: {strings}")  # Output: ['banana', 'apple', 'cherry']
print(f"Type of reversed_strings: {type(reversed_strings)}")  # Output: <class 'list_reverseiterator'>
print("-----------------------------------")
print()

stringintegers: List[Union[str, int]] = ["banana", "apple", "cherry", 5, 2, 9, 1, 5, 6]
print("strings: List[Union[str, int]] = [\"banana\", \"apple\", \"cherry\", 5, 2, 9, 1, 5, 6]")
print("Reversed Method Used List Of Strings And Integers")
print("-----------------------------------")
print("reversed_stringintegers = reversed(stringintegers)")
reversed_stringintegers = reversed(stringintegers)
print(f"Reversed String Integers: {list(reversed_stringintegers)}")  # Output: [6, 5, 1, 9, 2, 5, 'cherry', 'apple', 'banana']
print(f"Original String Integers: {stringintegers}")  # Output: ['banana', 'apple', 'cherry', 5, 2, 9, 1, 5, 6]
print(f"Type of reversed_stringintegers: {type(reversed_stringintegers)}")  # Output: <class 'list_reverseiterator'>
print("-----------------------------------")
print()

tuples: tuple = (5, 2, 9, 1, 5, 6)
print("tuples: tuple = (5, 2, 9, 1, 5, 6)")
print("Reversed Method Used Tuple Of Integers")
print("-----------------------------------")
reversed_tuples = reversed(tuples)
print("reversed_tuples = reversed(tuples)")
print(f"Reversed Tuples: {list(reversed_tuples)}")  # Output: [6, 5, 1, 9, 2, 5]
print(f"Original Tuples: {tuples}")  # Output: (5, 2, 9, 1, 5, 6)
print(f"Type of reversed_tuples: {type(reversed_tuples)}")  # Output: <class 'tuple_reverseiterator'>
print("-----------------------------------")
print()

dictionary: dict = {"banana": 3, "apple": 2, "cherry": 5}
print("dictionary: dict = {\"banana\": 3, \"apple\": 2, \"cherry\": 5}")
print("Reversed Method Used Dictionary")
print("-----------------------------------")
reversed_dictionary = reversed(dictionary)
print("reversed_dictionary = reversed(dictionary)")
print(f"Reversed Dictionary Keys: {list(reversed_dictionary)}")  # Output: ['cherry', 'apple', 'banana']
print(f"Original Dictionary Keys: {list(dictionary.keys())}")  # Output: ['banana', 'apple', 'cherry']
print(f"Type of reversed_dictionary: {type(reversed_dictionary)}")  # Output: <class 'dict_reverseiterator'>
print("-----------------------------------")
print()

set_of_numbers: set = {5, 2, 9, 1, 5, 6}
print("set_of_numbers: set = {5, 2, 9, 1, 5, 6}")
print("Reversed Method Used Set Of Integers")
print("-----------------------------------")
print(Fore.RED + "集合は順序がないため、reversed()関数を使用してセットを逆にすることはできません。")
try:
    print("reversed_set_of_numbers = reversed(set_of_numbers)")
    reversed_set_of_numbers = reversed(set_of_numbers)
except TypeError as e:
    print(f"Error: {e}", "Cannot reverse a set as it is unordered.")
print("-----------------------------------")
print()

string: str = "banana"
print("string: str = \"banana\"")
print("Reversed Method Used String")
print("-----------------------------------")
reversed_string = reversed(string)
print("reversed_string = reversed(string)")
print(f"Reversed String: {''.join(reversed_string)}")  # Output: 'ananab'
print(f"Original String: {string}")  # Output: 'banana'
print(f"Type of reversed_string: {type(reversed_string)}")  # Output: <class 'str_reverseiterator'>
print("-----------------------------------")
print()