from colorama import init, Fore
from collections import namedtuple

init(autoreset=True)

print()
print("namedtupleModule.py")
print()
print("Creating a namedtuple")
print("------------------------------------")
Person = namedtuple("Person", ["name", "age"])
print("Person = namedtuple(\"Person\", [\"name\", \"age\"])")
person1 = Person(name="Alice", age=30)
print("person1 = Person(name=\"Alice\", age=30)")
print("person1: ", person1)  # Output: Person(name='Alice', age=30)
print("person1.name: ", person1.name)  # Output: Alice
print("person1.age: ", person1.age)  # Output: 30
print("person1[0]: ", person1[0])  # Output: Alice
print("person1[1]: ", person1[1])  # Output: 30
print("------------------------------------")
print()
print("appending to namedtuple")
print("-------------------------------------")
person2 = Person("Bob", 25)
print("person2 = Person(\"Bob\", 25)")
print("person2: ", person2)  # Output: Person(name='Bob', age=25)
print("person1.name: ", person1.name)  # Output: Alice
print("person1.age: ", person1.age)  # Output: 30
print("person2.name: ", person2.name)  # Output: Bob
print("person2.age: ", person2.age)  # Output: 25
print("--------------------------------------")
print()
try:
    print("appending to namedtuple too many values")
    print("--------------------------------------")
    person3 = Person("Charlie", 40, "Extra Value")
    print("person3 = Person(\"Charlie\", 40, \"Extra Value\")")
    print("person3: ", person3)
    print("--------------------------------------")
except TypeError as e:
    print(f"TypeError: {e}", "Too many values to unpack for the namedtuple.")
print()
print("Updating namedtuple values")
print("--------------------------------------")
print(Fore.RED + "namedtupleはイミュータブルなため、属性を直接変更することはできません。")
try:
    print("person1.age = 40")
    person1.age = 40
except AttributeError as e:
    print(f"AttributeError: {e}", "Cannot assign to field 'age' of a namedtuple.")
print("--------------------------------------")
print()
print("_replace method used to update namedtuple values")
print("--------------------------------------")
updated_person1 = person1._replace(age=40)
print("updated_person1 = person1._replace(age=40)")
print("updated_person1: ", updated_person1)  # Output: Person(name='Alice', age=40)
print("original person1: ", person1)  # Output: Person(name='Alice', age=30)
print("--------------------------------------")
print()
print("asdict method used to convert namedtuple to dictionary")
print("person1._asdict(): ", person1._asdict())  # Output: {'name': 'Alice', 'age': 30}
print("type of person1._asdict(): ", type(person1._asdict()))  # Output: <class 'collections.OrderedDict'>
print("--------------------------------------")
print()
print("field names of namedtuple")
print("person1._fields: ", person1._fields)  # Output: ('name', 'age')
print("type of person1._fields: ", type(person1._fields))  # Output: <class 'tuple'>
print("--------------------------------------")
print()