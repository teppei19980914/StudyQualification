from colorama import init, Fore
import itertools

init(autoreset=True)

print()
print("itertoolsModule.py")
print()
print("Creating an Infinite Iterator")
print("------------------------------------")
iterator = itertools.chain(["A", "B"], "ab", range(3))
print("iterator = itertools.chain([\"A\", \"B\"], \"ab\", range(3))")
print("Iterator:", iterator)  # Output: <itertools.chain object at 0x...>
for item in iterator:
    print(item)  # Output: A, B, a, b, 0, 1, 2
print("Type of iterator:", type(iterator))  # Output: <class 'itertools.chain'>
print("-----------------------------------")
print()
print("Creating Grouped Iterator")
print("------------------------------------")
grouped_iterator = itertools.groupby("AAABBBCCDAA")
print("grouped_iterator = itertools.groupby(\"AAABBBCCDAA\")")
for key, group in grouped_iterator:
    print(f"Key: {key}, Group: {list(group)}")
    # Output:
    # Key: A, Group: ['A', 'A', 'A']
    # Key: B, Group: ['B', 'B', 'B']
    # Key: C, Group: ['C', 'C']
    # Key: D, Group: ['D']
    # Key: A, Group: ['A']
sorted_grouped_iterator = ''.join(sorted("AAABBBCCDAA"))
print("sorted_grouped_iterator = sorted(grouped_iterator)")
for key, group in itertools.groupby(sorted_grouped_iterator):
    print(f"Key: {key}, Group: {list(group)}")
    # Output:
    # Key: A, Group: ['A', 'A', 'A', 'A', 'A']
    # Key: B, Group: ['B', 'B', 'B']
    # Key: C, Group: ['C', 'C']
    # Key: D, Group: ['D']
print("-----------------------------------")
print()
print("Creating a Filtered Iterator")
print("------------------------------------")
filtered_iterator = itertools.groupby([10, 20, 31, 11, 3, 4], key=lambda x: x % 2 == 0)
print("filtered_iterator = itertools.groupby([10, 20, 31, 11, 3, 4], key=lambda x: x % 2 == 0)")
for key, group in filtered_iterator:
    print(f"Key: {key}, Group: {list(group)}")
    # Output:
    # Key: True, Group: [10, 20]
    # Key: False, Group: [31, 11, 3]
    # Key: True, Group: [4]
print("-----------------------------------")
print()
print("Creating a slice of an Infinite Iterator")
print("------------------------------------")
sliced_iterator = itertools.islice([10, 20, 31, 11, 3, 4], 3)
print("sliced_iterator = itertools.islice([10, 20, 31, 11, 3, 4], 3)")
print("Sliced Iterator:", sliced_iterator)  # Output: <itertools.islice object at 0x...>
for item in sliced_iterator:
    print(item)  # Output: 10, 20, 31
print("-----------------------------------")
print()
print("Creating a zip of Infinite Iterators")
print("------------------------------------")
zipped_iterator = zip("ABCD", [10, 20, 31], (11, 3, 4))
print("zipped_iterator = zip(\"ABCD\", [10, 20, 31], (11, 3, 4))")
print("Zipped Iterator:", zipped_iterator)  # Output: <zip object at 0x...>
for item in zipped_iterator:
    print(item)  # Output: ('A', '10', '11'), ('B', '20', '3'), ('C', '31', '4')
print("-----------------------------------")
print()
print("Creating a zip of Infinite Iterators with strict=True")
print("------------------------------------")
print(Fore.RED + "zip関数に「strict=True」を指定すると、各イテレータの長さが異なる場合にエラーが発生する")
try:
    zipped_iterator = zip("ABCD", [10, 20, 31], (11, 3, 4), strict=True)
    print("zipped_iterator = zip(\"ABCD\", [10, 20, 31], (11, 3, 4))")
    print("Zipped Iterator:", zipped_iterator)  # Output: <zip object at 0x...>
    for item in zipped_iterator:
        print(item)  # Output: ('A', '10', '11'), ('B', '20', '3'), ('C', '31', '4')
except ValueError as e:
    print(f"Error: {e}", "ValueError: zip() argument 1 is longer than argument 2")
print("-----------------------------------")
print()
print("Creating a longest zip of Infinite Iterators")
print("------------------------------------")
print(Fore.RED + "zip_longest関数は、fillvalueが指定されていないと、Noneで不足分を埋める")
longest_zipped_iterator = itertools.zip_longest("ABCD", [10, 20, 31], (11, 3, 4))
print("longest_zipped_iterator = itertools.zip_longest(\"ABCD\", [10, 20, 31], (11, 3, 4))")
print("Longest Zipped Iterator:", longest_zipped_iterator)  # Output: <itertools.zip_longest object at 0x...>
for item in longest_zipped_iterator:
    print(item)  # Output: ('A', '10', '11'), ('B', '20', '3'), ('C', '31', '4'), ('D', None, None)
print("-----------------------------------")
print()
print("Creating a longest zip of Infinite Iterators With fillvalue")
print("------------------------------------")
print(Fore.RED + "zip_longest関数は、最長のイテレータに合わせて、他のイテレータの不足分をfillvalueで埋める")
longest_zipped_iterator = itertools.zip_longest("ABCD", [10, 20, 31], (11, 3, 4), fillvalue="-")
print("longest_zipped_iterator = itertools.zip_longest(\"ABCD\", [10, 20, 31], (11, 3, 4), fillvalue=\"-\")")
print("Longest Zipped Iterator:", longest_zipped_iterator)  # Output: <itertools.zip_longest object at 0x...>
for item in longest_zipped_iterator:
    print(item)  # Output: ('A', '10', '11'), ('B', '20', '3'), ('C', '31', '4'), ('D', '-', '-')
print("-----------------------------------")
print()
print("Creating a product of Infinite Iterators")
print("------------------------------------")
product_iterator = itertools.product([10, 20])
print("product_iterator = itertools.product([10, 20])")
print("Product Iterator:", product_iterator)  # Output: <itertools.product object at 0x...>
for item in product_iterator:
    print(item)  # Output: (10,), (20,)
print("-----------------------------------")
print()
print("Creating a product of Infinite Iterators")
print("------------------------------------")
product_iterator = itertools.product([10, 20], repeat=2)
print("product_iterator = itertools.product([10, 20], repeat=2)")
print("Product Iterator:", product_iterator)  # Output: <itertools.product object at 0x...>
for item in product_iterator:
    print(item)  # Output: (10, 10), (10, 20), (20, 10), (20, 20)
print("-----------------------------------")
print()
print("Creating a product of Infinite Iterators")
print("------------------------------------")
product_iterator = itertools.product([10, 20], repeat=3)
print("product_iterator = itertools.product([10, 20], repeat=3)")
print("Product Iterator:", product_iterator)  # Output: <itertools.product object at 0x...>
for item in product_iterator:
    print(item)  # Output: (10, 10, 10), (10, 10, 20), (10, 20, 10), (10, 20, 20), (20, 10, 10), (20, 10, 20), (20, 20, 10), (20, 20, 20)
print("-----------------------------------")
print()
print("Creating a permutations of Infinite Iterators")
print("------------------------------------")
permutations_iterator = itertools.permutations("ABC")
print("permutations_iterator = itertools.permutations(\"ABC\")")
print("Permutations Iterator:", permutations_iterator)  # Output: <itertools.permutations object at 0x...>
for item in permutations_iterator:
    print(item)  # Output: ('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')
print("-----------------------------------")
print()
print("Creating a permutations of Infinite Iterators with r")
print("------------------------------------")
permutations_iterator = itertools.permutations("ABC", r=2)
print("permutations_iterator = itertools.permutations(\"ABC\", r=2)")
print("Permutations Iterator:", permutations_iterator)  # Output: <itertools.permutations object at 0x...>
for item in permutations_iterator:
    print(item)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
print("-----------------------------------")
print()
print("Creating a combinations of Infinite Iterators")
print("------------------------------------")
combinations_iterator = itertools.combinations("ABC", 2)
print("combinations_iterator = itertools.combinations(\"ABC\", 2)")
print("Combinations Iterator:", combinations_iterator)  # Output: <itertools.combinations object at 0x...>
for item in combinations_iterator:
    print(item)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'C')
print("-----------------------------------")
print()
print("Creating a combinations of Infinite Iterators with r")
print("------------------------------------")
combinations_iterator = itertools.combinations("ABC", r=2)
print("combinations_iterator = itertools.combinations(\"ABC\", r=2)")
print("Combinations Iterator:", combinations_iterator)  # Output: <itertools.combinations object at 0x...>
for item in combinations_iterator:
    print(item)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'C')
print("-----------------------------------")
print()
print("Creating a combinations with replacement of Infinite Iterators")
print("------------------------------------")
combinations_with_replacement_iterator = itertools.combinations_with_replacement("ABC", 2)
print("combinations_with_replacement_iterator = itertools.combinations_with_replacement(\"ABC\", 2)")
print("Combinations with Replacement Iterator:", combinations_with_replacement_iterator)  # Output: <itertools.combinations_with_replacement object at 0x...>
for item in combinations_with_replacement_iterator:
    print(item)  # Output: ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')
print("-----------------------------------")
print()