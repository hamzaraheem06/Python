# heading: Repetition statements allow us to execute same code block multiple times based on a boolean expression.

# define: for loop allow us to iterate over a sequence (i.e. list, tuple, range, set) in python. Its like a foreach loop in other programming languages 

#  syntax:
#   for i in sequence:
#       loop body 

# zen = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# '''

# for char in zen:
#     if char not in 'aeiou': # printing all the non-vowel letters
#         print(char, sep='', end='')

# seperate even and odd numbers from a list
# numbers = [34,54,67,21,78,97,45,44,80,19]
# even_numbers = []
# odd_numbers = []

# for num in numbers:
#     if num % 2: # flexy use of truthy and falsy concept if the remainder is zero which is equivalent to False anything else will make the condition True and hence they will be added to the odd list
#         odd_numbers.append(num)
#     else:
#         even_numbers.append(num)

# print("The even numbers are", even_numbers)
# print("The odd numbers are", odd_numbers)

# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for x in numbers.values():
#    print (x )

# note: what the actual fuck is for else loop? 
# define: for else loop first iterates the for block, and when the loop condition gets False, the else block is executed

# syntax:
# for i in sequence:
#     statements
# else: 
#     statements

# note: the else block is executed when the for loop terminates normally, if the loop is terminated midway due to break statement, the else block is not executed

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
else:
    print("5")

# define: while loop executes the set of statements as long as a defined expression is True

# syntax: 

# controling_var = X

# while controling_condition:
    # statements

# note: like for-else there is while-else too which is based on the  