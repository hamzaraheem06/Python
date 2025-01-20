import math as m
import random as r  

# math is a module which contains functions to perform various mathematical operations

# also the math module has commonly used constants like pi, e, and tau(2pi)

# >>> 2* m.pi == m.tau
#       True

# for more details: https://www.tutorialspoint.com/python/python_numbers.htm , and for quick look 

# note: random is also a module that provides random generator and other random operations
# i) random.choice(sequence) returns a random element from a sequence

# ii) random.randrange(start, stop, step) returns a random integer from the specified integer range [start, stop)

# iii) random.random() returns a random float value from [0, 1)

# iv) random.shuffle(seq) shuffles the element of seq randomly

# v) random.uniform(a, b)

# This function returns a random floating point value r, such that a is less than or equal to r and r is less than b i.e. [a, b)

numbers = []

import random as r

# default sum(seq, start) has two parameters, one is the sequence and the seecond is the starting value. 
# start is not the starting index. it is the initial value of the sum 

for i in range(0, 5):
    random_num = r.randrange(12, 33)
    numbers.append(random_num)

print(numbers)

print(sum(numbers))
