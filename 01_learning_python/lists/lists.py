# define: list is collection of elements, similar to Arrays in other languages but NOT an ARRAY;

# these are defining by enclosing in square brackets, an e.g. is 

my_list = ["item1", "item2", "item.....", "itemn"]

# any particular element can be accessed using the index in square bracker i.e. my_list[index]

# indexing methods like string can be used in lists also. i.e. slicing and all other

# since python is a dynamically typed language, the datatype of items need not to be same.

import random as rn

list = [ (lambda n: n * rn.randint(1, 10))(n) for n in range(10)] # for lambda part, refer to definition given in next section

new_list = [n for n in list if n >= 5]

# print(list)
# print(new_list)

# define: lambda functions are annonymous functions with no names 

# syntax: lambda params : expression 

# a single statment which will return something implicitly

# lar = lambda x,y: x if x > y else y

# # to immediately run a lambda function at its definition

# # enclose to function into parenthesis, and next to it pass the argument enclosed in parenthesis too
# # 
# # syntax: (lambda params : expression) (args) console.log: immediate lambda call

# larger = (lambda x, y: x if x > y else y)(12, 15)

# print(larger)
# print(lar(12, 17)) # 17

# define: nesting in comprehension syntax

my_list = [(x, y) for x in range(10) for y in range(10) if x > y]

# equivalent to:

# for x in range(10):
#     for y in range(10):
#         if x > y:
#             my_list.append((x, y))

# print(my_list)

# sorting of list

# note: a list is can be sorted using the built in sorted() function or .sort() method

# syntax: sorted(collection, key = function , reverse = bool)

# collection: any iterable 
# reverse: by default False, it set True sorts in reverse (descending) order

# key: is a function reference that allows us to set a custom comparison criteria

words = ['apple', 'banana', 'cherry', 'date']

# Sort by word length
sorted_words = sorted(words, key=len) # key = len means that the comparison will be bases on lenghts of the words i.e. it will map every element with its word lenght and then sort the length list and return the original sorted list mapped to the sorted lenght list

print(sorted_words)
# Output: ['date', 'apple', 'banana', 'cherry']

# note: copying a list, same deep copy and shallow copy crap. deep copy using .copy() method, slicing [:], comprehension 


# note: concatenation of list: done using +, .extend() method, and comprehension

# using comprehension 

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l = [item for sub in [l1, l2] for item in sub] 

# what this does

# for sub in [l1, l2]: # [l1, l2] = [[1, 2, 3], [4, 5, 6]]
#     for item in sub:
#         l.append(item)
     

