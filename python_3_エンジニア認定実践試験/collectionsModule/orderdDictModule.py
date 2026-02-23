from collections import OrderedDict
from colorama import init, Fore

init(autoreset=True)

print()
print("orderdDictModule.py")
print()
print("Creating an Dictionary")
print("------------------------------------")
print(Fore.RED + "Pythonの標準の辞書は、Python 3.7以降ではOrderedDictと同様に順序を保持します。")
my_dict = {}
print("my_dict = {}")
my_dict["apple"] = 1
print("my_dict[\"apple\"] = 1")
my_dict["banana"] = 2
print("my_dict[\"banana\"] = 2")
my_dict["orange"] = 3
print("my_dict[\"orange\"] = 3")
print("my_dict: ", my_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}
print("my_dict.keys(): ", my_dict.keys())  # Output: dict_keys(['apple', 'banana', 'orange'])
print("my_dict.values(): ", my_dict.values())  # Output: dict_values([1, 2, 3])
print("my_dict.items(): ", my_dict.items())  # Output: dict_items([('apple', 1), ('banana', 2), ('orange', 3)])
print("------------------------------------")
print()
print("Creating an OrderedDict")
print("------------------------------------")
print(Fore.RED + "OrderedDictは、Python 3.7以降の標準の辞書と同様の機能を提供します。")
ordered_dict = OrderedDict()
print("ordered_dict = OrderedDict()")
ordered_dict["apple"] = 1
print("ordered_dict[\"apple\"] = 1")
ordered_dict["banana"] = 2
print("ordered_dict[\"banana\"] = 2")
ordered_dict["orange"] = 3
print("ordered_dict[\"orange\"] = 3")
print("ordered_dict: ", ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
print("ordered_dict.keys(): ", ordered_dict.keys())  # Output: odict_keys(['apple', 'banana', 'orange'])
print("ordered_dict.values(): ", ordered_dict.values())  # Output: odict_values([1, 2, 3])
print("ordered_dict.items(): ", ordered_dict.items())  # Output: odict_items([('apple', 1), ('banana', 2), ('orange', 3)])
print("------------------------------------")
print()
print("Moveing an item to the end of the OrderedDict")
print("------------------------------------")
print(Fore.RED + "OderedDictは、指定したキーをOrderedDictの末尾に移動する「move_to_endメソッド」を提供します。")
ordered_dict.move_to_end("apple")
print("ordered_dict.move_to_end(\"apple\")")
print("ordered_dict: ", ordered_dict)  # Output: OrderedDict([('banana', 2), ('orange', 3), ('apple', 1)])
ordered_dict.move_to_end("apple", last=False)
print("ordered_dict.move_to_end(\"apple\", last=False)")
print("ordered_dict: ", ordered_dict)  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
print("------------------------------------")
print()
print("Difference between Dictionary and OrderedDict")
print("------------------------------------")
print(Fore.RED + "標準の辞書は、順序が異なる場合でも同じキーと値のペアを持つ限り、等しいと見なされますが、OrderedDictは、順序も考慮して等しいと見なされます。")
dict1 = {"apple": 1, "banana": 2, "orange": 3}
dict2 = {"banana": 2, "orange": 3, "apple": 1}
print("dict1: ", dict1)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}
print("dict2: ", dict2)  # Output: {'banana': 2, 'orange': 3, 'apple': 1}
print("dict1 == dict2: ", dict1 == dict2)  # Output: True
print("OrderedDict(dict1): ", OrderedDict(dict1))  # Output: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
print("OrderedDict(dict2): ", OrderedDict(dict2))  # Output: OrderedDict([('banana', 2), ('orange', 3), ('apple', 1)])
print("OrderedDict(dict1) == OrderedDict(dict2): ", OrderedDict(dict1) == OrderedDict(dict2))  # Output: False
print("------------------------------------")
print()
print("Poping Difference between Dictionary and OrderedDict")
print("------------------------------------")
print(Fore.RED + "OrderedDictは、popitemメソッドで、末尾のアイテムを削除して返すことができますが、標準の辞書は、一律最後の要素を削除して返します。")
print("ordered_dict: ", ordered_dict)  # Output: OrderedDict([('banana', 2), ('orange', 3), ('apple', 1)])
print("ordered_dict.popitem(): ", ordered_dict.popitem())  # Output: ('apple', 1)
print("ordered_dict.popitem(last=False): ", ordered_dict.popitem(last=False))  # Output: ('banana', 2)
print("ordered_dict: ", ordered_dict)  # Output: OrderedDict([('orange', 3)])
print("my_dict: ", my_dict)  # Output: {'apple': 1, 'banana': 2, 'orange': 3}
print("my_dict.popitem(): ", my_dict.popitem())  # Output: ('orange', 3) (順序が保証されないため、どのアイテムが削除されるかは不定)
print("my_dict: ", my_dict)  # Output: {'apple': 1, 'banana': 2} (順序が保証されないため、どのアイテムが削除されるかは不定)
print("my_dict.popitem(last=False): ")
try:
    print("my_dict.popitem(last=False): ", my_dict.popitem(last=False))  # Output: ('apple', 1) (順序が保証されないため、どのアイテムが削除されるかは不定)
except TypeError as e:
    print("Error:", e, "標準の辞書は、popitemメソッドでlast引数をサポートしていません。")
print("------------------------------------")
print()