# Python has primarily 6 built-in datatype categories.
# 
# 1. Numeric Datatypes
# i) int 
#      used to store an integer value like 5, 98, 1000, 100000, etc
# ii) float 
#      used to store decimal values like 9.8, 3.14, 3e12 etc
#      aeb = a * 10^b ( note: maximum limit = 1.79e308. Anything above that will give inf error. ) 
#      3e12 = 3 * 10^12 = 3000000000000.0
#      float.as_integer_ratio() : Returns a pair of integers whose ratio is exactly equal to the actual float having a positive denominator. In case of infinites, it raises overflow error and value errors on Not a number (NaNs).
# a = 3.5

# b = a.as_integer_ratio()  returns a tuple with two integers that gives the float value

# print(b) (7,2) 
# iii) complex
#      used to store complex values ( real + imaginary part values) e.g. 3 + 2j. these are written in a + bj format. 

# complex class has two built-in attributes, real and imag which return real and coefficient of imaginary part of the complex number respectively

# also there is a built-in conjugate function which returns the conjugate of a complex number

# a = 3 - 3j
# b = 8 + 4j

# print(a + b) (11+1j)
# iv) bool 
#       used to store a boolean value i.e. True or False. In python, we have to write this in Title case.

# 2) string datatype
    # also known as str 
a = "Hamza Raheem"
# character is accessed using its index(start from 0 and ends at #characters - 1) in square brackets.
# print(a[10]) e 
# print(type(a)) <class 'str'>
#   string in python are immutable, meaning you cannot change the character of the string indirectly, instead you produce a new string.

# a[1] = '12'

# TypeError: 'str' object does not support item assignment

# slice operator ([ ] and [start:end] )
# negative index mean starting from last -1 means last element and so on.
# print(a[1:]) amza Raheem
# print(a[:-1]) Hamza Rahee // slicing prints till the element before the end index 

# + can be used to concatenate two strings and * can be used to repeat the printing of the string


# print("Hamza","Raheem") Hamza Raheem
# print("Sniper! " * 3) Sniper! Sniper! Sniper! 
# print("Wifey! " * 3) Wifey! Wifey! Wifey! 

# 3. Sequence datatypes
#  collection datatype. similar to array in C++. accessed using the same square bracket method as in string. since, python is dynamically typed, we can store different type of values in sequence datatypes

# i) list 
    # note: [item1, item2, item3] defined by enclosing in square brackets and seperated by commas. 
    # similar accessing method is used, as does in string datatype. Also, concatenation can be done by + and repition using *

# myList = [["Hamza", 18, "Data Scientist", "NUST"], ["Muhammad Uzair", 18, "Data Scientist", "NUST"], ]
# print(myList)

# print("Displaying the student datalist:")
# for i in myList:
#     print(f"Name: {i[0]}\tAge: {i[1]}\tOccupation: {i[2]}\tUniversity: {i[3]}")

# print(myList) ['Hamza', 18, 'Data Scientist', 'NUST']
# print(myList[0]) Hamza
# print(myList[:]) ['Hamza', 18, 'Data Scientist', 'NUST']
# print(myList[2:]) ['Data Scientist', 'NUST']
# print(myList*2) ['Hamza', 18, 'Data Scientist', 'NUST', 'Hamza', 18, 'Data Scientist', 'NUST']

# ii) Tuple
    # similar to list it is defined using parenthesis. (item, item, item)
    # the main difference is that unlike list, it cannot be manipulated after declaration similar to string rules.
    # note: also called, read-only list

myTuple = ("Hamza", 18, "Data Scientist", "NUST")

# print(myTuple) ('Hamza', 18, 'Data Scientist', 'NUST')
# print(myTuple[0]) Hamza
# print(myTuple[:]) ('Hamza', 18, 'Data Scientist', 'NUST')
# print(myTuple[2:]) ('Data Scientist', 'NUST')
# print(myTuple*2) ('Hamza', 18, 'Data Scientist', 'NUST', 'Hamza', 18, 'Data Scientist', 'NUST')

# iii) Range 
#   range(start, stop, step) 
#   primarily used with loopss 
# for i in range(2,5,2):
#   print(i)

# 0
# 1
# 2
# 3
# 4

# 4. Dictionary datatype
    # note: dictionary is used to store data in key:value pairs. 
    # similar to objects in javascript.
    # key: can be any type but usually integer or a string. 
    # value: can be any type 
    # since it is not a sequence datatype like list or string so we cannot perform slicing operations

user = {
    "name": "Hamza Raheem",
    "age": 18,
    "Occupation": "Data Scientist"
    }

# accessed using bracket method similar to string. no dot method as in javascript
# print(user["name"])
user["University"] = "NUST"

# print(user)

user_bio_data = {
    "bloodType" : "A+",
    "adress": "Saidpur Model Village, Islamabad"
}

# print(user.keys()) dict_keys(['name', 'age', 'Occupation', 'University'])
# print(user.values()) dict_values(['Hamza Raheem', 18, 'Data Scientist', 'NUST'])

# print(user.__contains__("name"))

# 5. Set datatype
#      {element1, element2, element3}
#     set is the same as we have in mathematics. 
#     note: In python, set is used to store immutable datatypes. but itself is mutable
#     we cannot add a mutabble datatype in a set.
#       repetative values are ignored. 
#        note: not indexed datatype.
    

my_set = {"Hamza", 18, 2006, "Boy"}
# my_set = {"Hamza", 18, 2006, "Boy", myList} TypeError: unhashable type: 'list'
# print(type(my_set)) <class 'set'>

another_set ={1, 3, 21, 1, 34, 6, 2,3}

print(another_set)

# print(another_set) {1, 2, 34, 3, 21, 6}

# 6. Boolean datatype
# can be either True (1) or False (0)
# same concept of truthy and falsy is also implemented in python

# None is used to declared an uninitialized variable in python

x = None 
# print(type(x))


# primitive datatypes are the fundamental datatypes that lay foundation for the creation of complex data structures. These are int, float, boolean, string.

# non-primitive are collection of primitive datatypes. these are lists, dict, tuple, and sets. 
