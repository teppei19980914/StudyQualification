from collections import defaultdict

print()
print("defaultDictKeyModule.py")
print()
try:
    print("Dictionary Key Access")
    print("-----------------------------------")
    dictionary = {"a": 1, "b": 2, "c": 3}
    print("dictionary = {\"a\": 1, \"b\": 2, \"c\": 3}")
    result = dictionary["a"]
    print("result = dictionary[\"a\"]")
    print(result)  # Output: 1
    print("result = dictionary[\"d\"]")
    result = dictionary["d"]
    print(result)  # KeyError: 'd'
    print("-----------------------------------")
except KeyError as e:
    print(f"KeyError: {e}", "The key does not exist in the dictionary.")
finally:
    print()

print("defaultdict Key Access")
print("-----------------------------------")
def value():
    return 0
default_dict = defaultdict(value, spam=100)
print("default_dict = defaultdict(value, spam=100)")
result = default_dict["spam"]
print("result = default_dict[\"spam\"]")
print(result)  # Output: 100
print("存在しないキーを指定した場合、defaultdictは自動的にデフォルト値を生成して返します。")
result = default_dict["eggs"]
print("result = default_dict[\"eggs\"]")
print(result)  # Output: 0
print("default_dict after accessing non-existent key: ", default_dict)  # Output: defaultdict(<function value at 0x...>, {'spam': 100, 'eggs': 0})
print("type of default_dict: ", type(default_dict))  # Output: <class 'collections.defaultdict'>
print("-----------------------------------")
print()
print("Int Defaultdict")
print("-----------------------------------")
int_default_dict = defaultdict(int)
print("int_default_dict = defaultdict(int)")
print("int_default_dict[\"missing_key\"] = ", int_default_dict["Key"])  # Output: 0
int_default_dict["Key"] = 5
print("int_default_dict[\"Key\"] = 5")
print("int_default_dict[\"Key\"] = ", int_default_dict["Key"])  # Output: 5
int_default_dict["Key"] += 1
print("int_default_dict[\"Key\"] += 1")
print("int_default_dict[\"Key\"] = ", int_default_dict["Key"])  # Output: 6
print("int_default_dict after operations: ", int_default_dict)  # Output: defaultdict(<class 'int'>, {'Key': 6})
print("type of int_default_dict: ", type(int_default_dict))  # Output: <class 'collections.defaultdict'>
print("-----------------------------------")
print()
print("defaultdict with get")
print("-----------------------------------")
dd = defaultdict(int)
print("'x' in dd:", 'x' in dd)  # Output: False
print("dict(dd): ", dict(dd))  # Output: {}
print("dd.get('x'):", dd.get('x'))  # Output: None
print("dict(dd): ", dict(dd))  # Output: {}
print("dd['x']:", dd['x'])  # Output: 0
print("dict(dd): ", dict(dd))  # Output: {'x': 0}
print("'x' in dd:", 'x' in dd)  # Output: True
print("dict(dd): ", dict(dd))  # Output: {'x': 0}
print("-----------------------------------")
print()