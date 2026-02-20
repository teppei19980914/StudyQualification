import copy
from colorama import init, Fore

init(autoreset=True)

print()
print("copyModule.py")
print()
number_list = [1, 2, [1, [1, 2], 3], [4, [3, 4], 6], 5]
print("number_list = [1, 2, [1, [1, 2], 3], [4, [3, 4], 6], 5]")
print("Reference Copy of List")
print("-----------------------------------")
print(Fore.RED + "リストの参照コピーは、元のリストと同じオブジェクトを指すため、どちらかを変更すると両方に影響が出ます。")
reference_copy = number_list
print("reference_copy = number_list")
print("Reference Copy:", reference_copy)  # Output: [1, 2, 3, 4, 5]
print("Type of reference_copy:", type(reference_copy))  # Output: <class 'list'>
print("Modifying reference_copy by appending 6")
reference_copy.append(6)
print("Reference Copy after modification:", reference_copy)  # Output: [1, 2, 3, 4, 5, 6]
print("Original number_list after modification to reference_copy:", number_list)  # Output: [1, 2, 3, 4, 5, 6]
print("-----------------------------------")
print()
print("Reference Copy of int")
print("-----------------------------------")
print(Fore.RED + "整数の参照コピーは、元の整数と同じオブジェクトを指すため、どちらかを変更しても両方に影響が出ません。")
number = 10
print("number = 10")
reference_copy_number = number
print("reference_copy_number = number")
print("Reference Copy of Number:", reference_copy_number)  # Output: 10
print("Type of reference_copy_number:", type(reference_copy_number))  # Output: <class 'int'>
print("Modifying reference_copy_number by adding 5")
reference_copy_number += 5
print("Reference Copy of Number after modification:", reference_copy_number)  # Output: 15
print("Original number after modification to reference_copy_number:", number)  # Output: 10
print("-----------------------------------")
print()
print("Reference Copy of String")
print("-----------------------------------")
print(Fore.RED + "文字列の参照コピーは、元の文字列と同じオブジェクトを指すため、どちらかを変更しても両方に影響が出ません。")
string = "Hello"
print("string = \"Hello\"")
reference_copy_string = string
print("reference_copy_string = string")
print("Reference Copy of String:", reference_copy_string)  # Output: Hello
print("Type of reference_copy_string:", type(reference_copy_string))  # Output: <class 'str'>
print("Modifying reference_copy_string by adding \" World\"")
reference_copy_string += " World"
print("Reference Copy of String after modification:", reference_copy_string)  # Output: Hello World
print("Original string after modification to reference_copy_string:", string)  # Output: Hello
print("-----------------------------------")
print()
print("Shallow Copy of List")
print("-----------------------------------")
print(Fore.RED + "浅いコピーは、外側のコンテナは別物だが、内部の要素は同じ参照のままです。")
shallow_copy = copy.copy(number_list)
print("shallow_copy = copy.copy(number_list)")
print("Shallow Copy:", shallow_copy)  # Output: [1, 2, 3, 4, 5, 6]
print("Type of shallow_copy:", type(shallow_copy))  # Output: <class 'list'>
print("Modifying shallow_copy by appending 7")
shallow_copy.append(7)
print("Shallow Copy after modification:", shallow_copy)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("Original number_list after modification to shallow_copy:", number_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("-----------------------------------")
print()
print("Deep Copy of List")
print("-----------------------------------")
print(Fore.RED + "リストの深いコピーは、元のリストと異なるオブジェクトを指すため、どちらかを変更しても両方に影響が出ません。")
deep_copy = copy.deepcopy(number_list)
print("deep_copy = copy.deepcopy(number_list)")
print("Deep Copy:", deep_copy)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("Type of deep_copy:", type(deep_copy))  # Output: <class 'list'>
print("Modifying deep_copy by appending 8")
deep_copy.append(8)
print("Deep Copy after modification:", deep_copy)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print("Original number_list after modification to deep_copy:", number_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("-----------------------------------")
print()
print("Reference Copy And Shallow Copy And Deep Copy")
print("-----------------------------------")
print(Fore.RED + "リストの参照コピーは元のリストと同じオブジェクトを指すが、浅いコピー/深いコピーは異なるオブジェクトを指します。")
reference_copy_list = number_list
print("reference_copy_list = number_list")
shallow_copy_list = copy.copy(number_list)
print("shallow_copy_list = copy.copy(number_list)")
deep_copy_list = copy.deepcopy(number_list)
print("deep_copy_list = copy.deepcopy(number_list)")
print("number_list is reference_copy_list: ", number_list is reference_copy_list)  # Output: True
print("number_list is shallow_copy_list: ", number_list is shallow_copy_list)  # Output: False
print("number_list is deep_copy_list: ", number_list is deep_copy_list)  # Output: False
print("------------------------------------")
print()
print("Shallow Copy And Deep Copy")
print("-----------------------------------")
print(Fore.RED + "リストの浅いコピーは元のリストとオブジェクトは異なるが、リスト内の要素は同じオブジェクトを指す。深いコピーはリスト内の要素も異なるオブジェクトを指す。")
print("number_list[0] is shallow_copy_list[0]: ", number_list[0] is shallow_copy_list[0])  # Output: True
print("number_list[2] is deep_copy_list[2]: ", number_list[2] is deep_copy_list[2])  # Output: False
print("---------------------------------")
print()
print("update original list")
number_list.append(9)
print("number_list after update:", number_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 9]
print("reference_copy_list after update:", reference_copy_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 9]
print("shallow_copy_list after update:", shallow_copy_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("deep_copy_list after update:", deep_copy_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
print("---------------------------------")
print()
print("Shallow Copy")
print("-----------------------------------")
slice = number_list[:]
print("slice = number_list[:]")
list_copy = list(number_list)
print("list_copy = list(number_list)")
copy_copy = copy.copy(number_list)
print("copy_copy = copy.copy(number_list)")
print("slice is number_list: ", slice is number_list)  # Output: False
print("list_copy is number_list: ", list_copy is number_list)  # Output: False
print("copy_copy is number_list: ", copy_copy is number_list)  # Output: False
print(slice[0] is number_list[0])  # Output: True
print(list_copy[0] is number_list[0])  # Output: True
print(copy_copy[0] is number_list[0])  # Output: True
print("-----------------------------------")
print()