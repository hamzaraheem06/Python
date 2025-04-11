# define: tuple is a built in collection datatype. it is an immutable list.

# defined by comma seperated items enclosed in parenthesis

# every thing in tuple is similar but the only difference is that you cannot reassign the value after declaration

my_tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# del my_tup[9] # tuple cannot be mutated. all the assigning operations are atomically not allowed.

# updation using comprehension

# you first have to convert the tuple to a list, perfrom the comprehension operation, and then convert it back to tuple

inter = list(my_tup)

inter = [n*100 for n in inter]

my_tup = tuple(inter) # immutability means that reference can change but not it's content, here we are changing the reference of my_tup not assigning a value

print(my_tup) 

# note: all the list methods can be applied to a tuple, this is done by first converting the tuple to list, do your operation and then convert back to tuple 

# define: The term "unpacking" refers to the process of parsing tuple items in individual variables.

m = (1, 4) # literal representation
t = 1, 4 # also a valid representation

# print(type(t), type(m), sep='\t') # <class 'tuple'> <class 'tuple'>

# unpacking the elements of tuple into individual variables 
m = (1, 4, 5)
# x, y, z = m 

# print("x: " , x , 'y: ' , y) # x:  1 y:  4

# note: the number of variables and size of tuple must be same, else it will give error

m = (1, 4, 5)
# x, y, z, w = m # ValueError: not enough values to unpack (expected 4, got 3)

# to assign a collection to elements to unpacking variable using asterick with it to mention that this is a list.

m = (1, 4, 5)

x , *y = m

print("x: " , x , 'y: ' , y) # x:  1 y:  [4, 5]

# even if you write the * at the first var, the python will make sure that each gets a value

*x , y = m

print("x: " , x , 'y: ' , y) # x:  [1, 4] y:  5

#note: multiple asterisks are not allowed

