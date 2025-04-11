# define: sets are an unordered collection of elements, implemented to provide sets as in mathematics

# defined using seperated by commas in {} or passing a collection in set() 

# sets have similar kind of methods as lists or other collection, the difference that sets have, even in mathematics that sets donot contain duplicates and order of elements doesn't matter so no indexing in sets

# just remember to use .discard() to remove element instead of .remove() normally because .remove() raises error if the element is not in set

# comprehension is same in sets as in list

my_set = {12, 23, 43, 3, 23}

double_set = {n*2 for n in my_set if n > 20}

# print(double_set) # {46, 86}

# define: frozen sets are set defined using frozenset() function, that are immutable after declaration. These donot allow reassignment of elements after declaration or deleting any element similar to tuples

import itertools 

# print({subset for subset in itertools.combinations(my_set, 5)}) # {(43, 3, 23), (43, 3, 12), (43, 12, 23), (3, 12, 23)} generating r element subsets of a set: itertools.combinations(set, r)

# syntax: Adding of elements
# note: adding element in set: .add(element) to add a single element
# note:adding multiple elements in set: .update(collection) to add multiple elements at once in a set

langs = {"C++", "C", "Java", "JavaScript", "Python"} 

langs.add("Rust") # adds one element
langs.add("Ruby") # adds one element

new_langs = {"R", "C#", "GoLang", "Bash", "BhaiLang"}

# langs.update(new_langs) # adds to whole new collection (i.e. set) to the original set

# print(langs) # {'Rust', 'GoLang', 'Ruby', 'JavaScript', 'C++', 'C#', 'BhaiLang', 'C', 'Java', 'Bash', 'R', 'Python'}

# note: adding using union: .union() method or | are used to perform union operation on two elements

langs = langs.union(new_langs) # or langs = langs | new_langs

# print(langs) # {'Java', 'R', 'C#', 'C++', 'BhaiLang', 'GoLang', 'Rust', 'Bash', 'Ruby', 'Python', 'C', 'JavaScript'}

# syntax: traversing a set 
# note: using for loop

# for lang in langs:
#     print(lang, end='\t') # Java    C++     GoLang  C       Rust    Bash    BhaiLang        C#      Ruby    R       JavaScript      Python

# note: using iter with a while loop

element = iter(langs)

# print(element) <set_iterator object at 0x000001771080E740>

# while True:
#     try: 
#         # print(next(element), end='\t') # Python  GoLang  BhaiLang        C#      Ruby    Rust    R       JavaScript      Bash    C       C++     Java 
#         # after all the values have been accessed the next access will incur error which will be handled by the except block
#     except:
#         break

# note: using set comprehension: which is similar as in list

# note: using enumerate() 

# for item in enumerate(langs): # returns a tuple with two elements: (index, value)
#     print("item", item)

# item (0, 'C#')
# item (1, 'Bash')
# item (2, 'Python')
# item (3, 'Java')
# item (4, 'BhaiLang')
# item (5, 'Rust')
# item (6, 'C')
# item (7, 'JavaScript')
# item (8, 'Ruby')
# item (9, 'C++')
# item (10, 'R')
# item (11, 'GoLang')

# for index, item in enumerate(langs): # unpacking the values of the tuple
#     print("index: ", index, "item: ", item)

# index:  0 item:  C++
# index:  1 item:  BhaiLang
# index:  2 item:  Python
# index:  3 item:  Java
# index:  4 item:  Ruby
# index:  5 item:  JavaScript
# index:  6 item:  GoLang
# index:  7 item:  R
# index:  8 item:  C
# index:  9 item:  C#
# index:  10 item:  Bash
# index:  11 item:  Rust

# define: set operators

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# syntax: union ( | )

union_set = set1 | set2
# print(union_set) {1, 2, 3, 4, 5, 6, 7, 8}

# syntax: intersection ( & )

intersect_set = set1 & set2
# print(intersect_set) {4, 5}

# syntax: difference ( - )

difference_set = set1 - set2
# print(difference_set) {1, 2, 3}

# syntax: subset (<=) a <= b means a is a subset of b

a = {1, 2, 3}

# print("a is subset of set1", a <= set1) a is subset of set1 True
# print("a is subset of set2", a <= set2) a is subset of set2 False
