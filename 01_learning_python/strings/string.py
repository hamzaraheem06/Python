# define: String is a sequence of characters in any programming language. These are used to store texts mostly.

# can be defined by enclosing in ' ', " " or """  """

my_string = "Hello, this is Hamza"

print(my_string)

# note: slicing a string: slicing means taking out portion of a string, this is done using indexes of string

# Syntax: str_identifier[start: stop: increment/decrement (optional)]

name = my_string[15: ] # or my_string[15: : 1]

# this is equivalent to in javascript

# for(int i = 15: i < my_string.length; i++) {
#     console.log(my_string[i])
# }

print(name) # Hamza

# note: to print in reverse 

reverse_name = name[::-1] # or name[len(name): : -1]

print(reverse_name) # azmaH

# note: replace a word/sequence of character .replace("stringToBeReplaced", "replacingValue") -> returns a new string with replaced literal

message = "Hello this is Hamza"

print(message.replace("Hamza", "Humzuh")) # Hello this is Humzuh, if the string to be replaced is not found, the original unchanged string will be return

print(message) # Hello this is Hamza

# Original string is same, because strings are immutable so the replace functions returns a new string, not modifying the orignal value

new_message = message.replace("Hamza", "Humzuh") #

print(new_message) # Hello this is Humzuh
print(message) # Hello this is Hamza


# note: splitting a text into peices of a list: .split("character") -> returns a list, which contains elements splitted on the basis of passing character 

names = "Hamza, Ayesha, Zainab, Javeria, Bushra"

names_list = names.split(",")
print(names_list) # ['Hamza', ' Ayesha', ' Zainab', ' Javeria', ' Bushra']

# note: finding the first occurance of a string or character: .find('ch/string') returns the index of the first occuring the ch/string, returns -1 if the element is not in the string

print(message.find('Hamza')) # 14 means the substring 'Hamza' starts from 14th index
print(message.find('hamza')) # -1

# note: To count the number of occurances of a substring: .count("substring") returns the number of times the substring has appeared in a string

my_greetings = "Hello Hello bol k, mery aaju baaju dol k."

print(my_greetings.count("Hello")) # 2

print(my_greetings.count("Hamza")) # 0

# note: formating a string

greetings = "Hello! This is {}, How may I help you, Ms. {}".format("Hamza", "Ayesha")
print(greetings)

# create a string from a list

my_courses = ["OOP", "DBS", "MVC", "LA", "DLD"]

hamza_courses = ", ".join(my_courses) # "seperator between elements".join(Iterable) -> returns a string that concatenates list items with seperator element between them

print(hamza_courses) # 'OOP, DBS, MVC, LA, DLD'

hamza_courses = "-".join(my_courses)

print(hamza_courses) # 'OOP-DBS-MVC-LA-DLD'

print(hamza_courses.__contains__("DM")) # False

# or you can use the in operator

print("DM" in hamza_courses) # False

# previously, we saw how to remove whitespaces. now lets add whitespaces or any other character to make a string to a desired lenght. note: .center(width, "ch") returns a string padded by character on both sides to make the lenght = width

name = "hamza"

name = name.title().center(11, "~") # name = '~~~Hamza~~~' 

print(name) # ~~~Hamza~~~
# doesnt modify if the lenght of the string is greater than the width value passed

# that's it with string in python. Solve few examples and slay strings in use.