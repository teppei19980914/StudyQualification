from colorama import init, Fore
import enum

init(autoreset=True)

print()
print("enumModule.py")
print()
print("Creating an Enum")
print("------------------------------------")
class Nengo(enum.Enum):
    SHOWA = 1
    HEISEI = 2
    REIWA = 3
print("""
class Nengo(enum.Enum):
    SHOWA = 1
    HEISEI = 2
    REIWA = 3
""")
class Weekday(enum.Enum):
    MONDAY = enum.auto()
    TUESDAY = enum.auto()
    WEDNESDAY = enum.auto()
    THURSDAY = enum.auto()
    FRIDAY = enum.auto()
print("""
class Weekday(enum.Enum):
    MONDAY = enum.auto()
    TUESDAY = enum.auto()
    WEDNESDAY = enum.auto()
    THURSDAY = enum.auto()
    FRIDAY = enum.auto()
""")
@enum.unique
class status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
print("""
@enum.unique
class status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
""")
try:
    print(Fore.RED + "「@enum.unique」デコレーターは、Enumクラス内のメンバーが一意であることを保証するために使用されます。重複する値がある場合、ValueErrorが発生します。")
    print("""
@enum.unique
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 2
    """)
    @enum.unique
    class Color(enum.Enum):
        RED = 1
        GREEN = 2
        BLUE = 2
except ValueError as e:
    print(f"ValueError: {e}", "Duplicate values are not allowed in an Enum decorated with @enum.unique.")

print()
print("Accessing Enum Members")
print("------------------------------------")
print("Nengo.SHOWA:", Nengo.SHOWA)
print("Nengo['HEISEI']:", Nengo['HEISEI'])
print("Nengo(3)", Nengo(3))
print("weekday.MONDAY.name:", Weekday.MONDAY.name)
print("weekday.TUESDAY.value:", Weekday.TUESDAY.value)
statuslist = list(status)
print("list(status):", statuslist)
print("------------------------------------")
print()
print("Comparing Enum Members")
print("------------------------------------")
print("Nengo.SHOWA == Nengo.SHOWA:", Nengo.SHOWA == Nengo.SHOWA)  # Output: True
print("Nengo.SHOWA == Nengo.HEISEI:", Nengo.SHOWA == Nengo.HEISEI)  # Output: False
print("Nengo.SHOWA is Nengo.SHOWA:", Nengo.SHOWA is Nengo.SHOWA)  # Output: True
print("Nengo.SHOWA is Nengo.HEISEI:", Nengo.SHOWA is Nengo.HEISEI)  # Output: False
print("Nengo.SHOWA == 1:", Nengo.SHOWA == 1)  # Output: False
print("Nengo.SHOWA.value == 1:", Nengo.SHOWA.value == 1)  # Output: True
print("Nengo.SHOWA.value == '1':", Nengo.SHOWA.value == '1') # Output: False
class CopyNengo(enum.Enum):
    SHOWA = 1
    HEISEI = 2
    REIWA = 3
print("""
class CopyNengo(enum.Enum):
    SHOWA = 1
    HEISEI = 2
    REIWA = 3
""")
print("Nengo.SHOWA == CopyNengo.SHOWA:", Nengo.SHOWA == CopyNengo.SHOWA)  # Output: False
print("Nengo.SHOWA is CopyNengo.SHOWA:", Nengo.SHOWA is CopyNengo.SHOWA)  # Output: False
print("------------------------------------")
print()
print("int Enum")
print("------------------------------------")
print("""
class IntEnum(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = "a"
""")
try:
    class IntEnum(enum.IntEnum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = "a"
except ValueError as e:
    print(f"ValueError: {e}", "All members of an IntEnum must be integers.")
print("""
class StrEnum(enum.StrEnum):
    A = "a"
    B = "b"
    C = "c"
    D = 1
""")
try:
    class StrEnum(enum.StrEnum):
        A = "a"
        B = "b"
        C = "c"
        D = 1
except ValueError as e:
    print(f"ValueError: {e}", "All members of an StrEnum must be strings.")
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = "a"
print("""
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = "a"
""")
try:
    print(Fore.RED + "「Color[5]」は、Color Enumに存在しないキーを指定したため、KeyErrorが発生します。")
    print("Color[5]:")
    print(Color[5])
except KeyError:
    print("KeyError: 5 is not a valid key in Color enum")
try:
    print(Fore.RED + "「Color.BLACK」は、Color Enumに存在しないメンバーを指定したため、AttributeErrorが発生します。")
    print("Color.BLACK")
    print(Color.BLACK)
except AttributeError:
    print("AttributeError: BLACK is not a valid member of Color enum")
try:
    print(Fore.RED + "「Color(4)」は、Color Enumに存在しない値を指定したため、ValueErrorが発生します。")
    print("Color(4)")
    print(Color(4))
except ValueError:
    print("ValueError: 4 is not a valid value in Color enum")
print("-------------------------------------")
print()
print("Int Enum")
print("--------------------------------------")
print(Fore.RED + "IntEnumは、Enumのサブクラスで、整数値を持つ列挙型を定義するために使用されます。IntEnumのメンバーは整数値を持ち、整数と比較することができます。")
class weekday(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
print("""
class weekday(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
""")
print("weekday.MONDAY == 1:", weekday.MONDAY == 1)  # Output: True
print("weekday.MONDAY is 1:", weekday.MONDAY is 1)  # Output: False
print("-------------------------------")
print()
print("Str Enum")
print("--------------------------------------")
print(Fore.RED + "StrEnumは、Enumのサブクラスで、文字列値を持つ列挙型を定義するために使用されます。StrEnumのメンバーは文字列値を持ち、文字列と比較することができます。")
class Status(enum.StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
print("""
class Status(enum.StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
""")
print("Status.PENDING == 'pending':", Status.PENDING == 'pending')  # Output: True
print("Status.PENDING is 'pending':", Status.PENDING is 'pending')  # Output: False
print("--------------------------------------")
print()