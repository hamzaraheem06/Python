# define: function is collection of reuseable code instructions that perform a specific operation.

# These make computer program more modular, reusable and efficient.

# syntax:
# def function_name( parameters ):
#    "function_docstring" # optional
#    function_body
#    return [expression]

# hamza you know what functions are.. so yeah. just watch a video on functions for python experience of it.

# define: Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.

# An anonymous function cannot be a direct call to print because lambda requires an expression

# Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

# syntax: 
# lambda [arg1 [,arg2,.....argn]]:expression

# sum = lambda x, y : x + y
#
# print(sum(12, 23))

# **kwargs are special type of arguments that accept variable number of key-value arguments. These are similar to the *args arguments but **kwargs accept key-value pairs too.

# def print_data(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}", end="\t")
#
#     print()
#
# print_data(name = "Hamza", age = 18, career = "BS Data Science")
#
# print_data(name = "Shampoo", quantity = 19, supplier = "Dove", total = 812.23)

# name: Hamza	age: 18	career: BS Data Science
# name: Shampoo	quantity: 19	supplier: Dove	total: 812.23

# yield keyword: it has a similar concept as static in many languages. In python, it can return the value from a function while also saving if's state in the memory. for example, you have to return numbers from a function one by one, by once the value is returned using the return keyword the function terminates and when you call the function next time, the function state is new. i.e. it is a new call. to deal with these kind of cases, the yield keyword is used with the variable to enable it to return its value and to also remember it's state in the memory.

# def even_generator(upper_bound):
#     for i in range(2, upper_bound + 1, 2):
#         yield i
#
# for num in even_generator(7):
#     print(num)

# 2
# 4
# 6

def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

print(fact(4))

# to access global variable instead of local variable in a scope, use the global keyword to specify that we are refereing to the global instance of this variable

a = 12

def func():
    global a
    a = 11

print(a) # 12
func()
print(a) # 11

# this is just for knowledge, avoid doing such practices.