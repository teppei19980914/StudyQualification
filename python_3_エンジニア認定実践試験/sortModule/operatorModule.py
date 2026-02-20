from operator import itemgetter, attrgetter
from typing import List

print()
print("operatorModule.py")
print()
data: List[tuple] = [("apple", 5), ("banana", 2), ("cherry", 8), ("berry", 3), ("apple", 2)]
print("data: List[tuple] = [(\"apple\", 5), (\"banana\", 2), (\"cherry\", 8), (\"berry\", 3), (\"apple\", 2)]")
print("Sorted Method Used List Of Tuples")
print("------------------------------------")
sorted_data = sorted(data)
print("sorted_data = sorted(data)")
print(f"sorted_data = {sorted_data}")  # Output: [('apple', 5), ('banana', 2), ('cherry', 8)]
print(f"Type of sorted_data: {type(sorted_data)}")  # Output: <class 'list'>
print("------------------------------------")
print()
print("Sorted Method Used List Of Tuples With itemgetter")
sorted_by_name = sorted(data, key=itemgetter(0))
print("sorted_by_name = sorted(data, key=itemgetter(0))")
print(f"sorted_by_name = {sorted_by_name}") # Output: [('apple', 5), ('apple', 2), ('banana', 2), ('berry', 3), ('cherry', 8)]
sorted_by_value = sorted(data, key=itemgetter(1))
print("sorted_by_value = sorted(data, key=itemgetter(1))")
print(f"sorted_by_value = {sorted_by_value}") # Output: [('apple', 2), ('banana', 2), ('berry', 3), ('apple', 5), ('cherry', 8)]
sorted_by_name_value = sorted(data, key=itemgetter(1, 0))
print("sorted_by_name_value = sorted(data, key=itemgetter(1, 0))")
print(f"sorted_by_name_value = {sorted_by_name_value}") # Output: [('apple', 2), ('banana', 2), ('berry', 3), ('apple', 5), ('cherry', 8)]
print("------------------------------------")
print()

dictionary: dict = {"apple": 5, "banana": 2, "cherry": 8, "berry": 3}
print("dictionary: dict = {\"apple\": 5, \"banana\": 2, \"cherry\": 8, \"berry\": 3}")
print("Sorted Method Used Dictionary With itemgetter")
sorted_dict_by_key = sorted(dictionary.items(), key=itemgetter(0))
print("sorted_dict_by_key = sorted(dictionary.items(), key=itemgetter(0))")
print(f"sorted_dict_by_key = {sorted_dict_by_key}") # Output: [('apple', 5), ('banana', 2), ('berry', 3), ('cherry', 8)]
sorted_dict_by_value = sorted(dictionary.items(), key=itemgetter(1))
print("sorted_dict_by_value = sorted(dictionary.items(), key=itemgetter(1))")
print(f"sorted_dict_by_value = {sorted_dict_by_value}") # Output: [('banana', 2), ('berry', 3), ('apple', 5), ('cherry', 8)]
print("------------------------------------")
print()

list_of_dicts: List[dict] = [{"name": "apple", "value": 5}, {"name": "banana", "value": 5}, {"name": "cherry", "value": 8}, {"name": "banana", "value": 3}]
print("list_of_dicts: List[dict] = [{\"name\": \"apple\", \"value\": 5}, {\"name\": \"banana\", \"value\": 5}, {\"name\": \"cherry\", \"value\": 8}, {\"name\": \"banana\", \"value\": 3}]")
print("Sorted Method Used List Of Dictionaries With itemgetter")
sorted_list_of_dicts_by_name = sorted(list_of_dicts, key=itemgetter("name"))
print("sorted_list_of_dicts_by_name = sorted(list_of_dicts, key=itemgetter(\"name\"))")
print(f"sorted_list_of_dicts_by_name = {sorted_list_of_dicts_by_name}") # Output: [{'name': 'apple', 'value': 5}, {'name': 'banana', 'value': 5}, {'name': 'berry', 'value': 3}, {'name': 'cherry', 'value': 8}]
sorted_list_of_dicts_by_value = sorted(list_of_dicts, key=itemgetter("value"))
print("sorted_list_of_dicts_by_value = sorted(list_of_dicts, key=itemgetter(\"value\"))")
print(f"sorted_list_of_dicts_by_value = {sorted_list_of_dicts_by_value}") # Output: [{'name': 'banana', 'value': 5}, {'name': 'berry', 'value': 3}, {'name': 'apple', 'value': 5}, {'name': 'cherry', 'value': 8}]
sorted_list_of_dicts_by_value_name = sorted(list_of_dicts, key=itemgetter("name", "value"))
print("sorted_list_of_dicts_by_value_name = sorted(list_of_dicts, key=itemgetter(\"name\", \"value\"))")
print(f"sorted_list_of_dicts_by_value_name = {sorted_list_of_dicts_by_value_name}") # Output: [{'name': 'apple', 'value': 5}, {'name': 'banana', 'value': 5}, {'name': 'berry', 'value': 3}, {'name': 'cherry', 'value': 8}]
print("------------------------------------")
print()