# # operators are symbols used to perform specific operations on operands. 
# # operands are variables or expressions on which operation are to be performed. 
# # types of operators:
# # i) Unary operator
#     # operators that work with only one operand 
# # ii) Binary Operator
#     # operators that work with two operands

# a = 10
# b = 12

#note: print("{} + {} = {}".format(a, b, a+b)) # C like format. 10 + 12 = 22

# # it can also be written like
# # print(f"{a} + {b} = {a+b}") 10 + 12 = 22 

# # Logical operators: These operators are used to combine two or more logical expressions(true or false statements). These are and, or, not.

# logical operator with numbers

# and:

# Evaluates operands from left to right.
# note: and Returns the first falsy value it encounters. If all values are truthy, it returns the last operand.
# or:

# Evaluates operands from left to right.
# note: or Returns the first truthy value it encounters. If all values are falsy, it returns the last operand.

# # Membership operators: These are used to check the existance of a variable in a sequence i.e. tuple, list, string. These are "in" (to check if the variable is present in the sequence) and "not in" ( to check that the variable is not in the sequence)

# if you try to check if two successive numbers are present in a list or tuple, the in operator returns False. If the list/tuple contains the successive numbers as a sequence itself, then it returns True.

var = ((10,20),30,40)
a = 10
b = 20
# print ((a,b), "in", var, ":", (a,b) in var) True 

# Python checks the membership only with the collection of keys and not values. 

# numbers = sorted([12, 1, 5, 3, 6, 12]) # to initialize when sorting
# # numbers.sort() to sort after
# # print(numbers)

# debug: a = a + b 

# # print(3.0 in numbers)

# shortListedNumbers = [1, 5]

# # for i in range(0, len(shortListedNumbers)):
#     # print(shortListedNumbers[i] in numbers)

# name = "Hamza Raheem"

# print("Abdul" not in name) # True

# Identity operators: Python identity operators compare the memory locations of two objects. these are used to check if two operators are the same instances. 
# note: These are "is" (to check if they are same meaning if they are same memory location) and "is not" ( to check if there are not same instances meaning they are different memory locations).

# # these are used to compare memory locations and not values, for example

# a = 12
# b = 12 
# c = a

# # print(a is b) True, how?
# # print(a is c) True 

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# c = a

# # print(a is c) True 
# # print(a is b) False

# # print(a is not c)
# # print(a is not b) 

# # new_numbers = numbers

# # print(new_numbers is numbers)

# ******************Calculator***********************

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

# operator = input("What arithmetic operation? ")

# 12e12 = 12 * 10**12

# name = "Hamza".tran 

# match is used to evaluate value of a variable as switch in another languages.

# syntax is almost same, except that there is no requirement of break statement and write case _: for default case. Rest of the logic is similar to original switch statement.

# match (operator): 
    # case "+":
    #     print(f"{num1} + {num2} = {num1 + num2}")
    # case "-":
    #     print(f"{num1} - {num2} = {num1 - num2}")
    # case "*":
    #     print(f"{num1} * {num2} = {num1 * num2}")
    # case "/":
    #     print(f"{num1} / {num2} = {num1 / num2}")
    # case "%":
    #     print(f"{num1} % {num2} = {num1 % num2}")
    # case "//":
    #     print(f"{num1} // {num2} = {num1 // num2}")
    # case "**":
    #     print(f"{num1} ** {num2} = {num1 ** num2}")
    # case _: # there is no keyword for default case in python, just write _ for the default case. note:
    #     print("Please enter a valid arithmetic operator")

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is b)

# # Printing IDs of a, b, and c
# print("id(a) : ", id(a))
# print("id(b) : ", id(b))
# print("id(c) : ", id(c))

# # Comparing and printing return values
# print(a is c)
# print(a is b)

name = input("What's your name? ")

dept = input("Enter your department: ")

print(f"Hello {name}, Welcome to {dept} department!")

a = 12
b = 12.1

