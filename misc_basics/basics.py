# print("Hello World")

# for i in range(1, 10, 3):
#     print("Even" if i%2 == 0 else "Odd")
#
# formatted string
# Hamza, like in javascript you can use `` to inject variables in a string, in Python you can do that by using f with the starting quotation of the string to tell the compiler this is a special type of string that you want to format in your way.

# name = input("What is your name? ").strip().title() input is a function that allow us to take an input value from the user. It returns whatever user types in a str format.
#
# nameSize = len(name)

# print(f"Hello, {name}") # print is a function that allow us to write some value on the terminal
# print(name.count('a', 0, len(name))) for counting the number of times a substring occurs in a string
# print(name.endswith('b')) # to check if a string ends with a specific character(s), you can also use this for a specific location in the string with start and end parameters.
# print("H\tA\tM\tZ\tA".expandtabs(tabsize=8)) Hamza you are intelligent you can understand this

# name = input("What is your name? ").strip()
# print(name.isalpha())

# name = "Hamza Raheem"
# names = [first, last] = name.split(" ")
# print(names[1])

# print(name.rfind('a', 0, len(name))) finds looks for a specific character(s) in a string, returns the index of the first instance, else returns -1 if there is no instance of the character(s) in the string

# message = "Hello, Hamza!"
# print(message)

# **********Python Crash Course*************
# Exercise 2.1 and 2.2
# message = "Hello, Hamza"
# print(message)
#
# message = "Hello, Ayesha"
# print(message)

# title = "how to fail at almost everything, and still win big".title()
#
# auther = "Micheal Jackson"
#
# titleAuther = title.join(auther)
#
# print(titleAuther)

# Exercise 2.3 - 2.7
# name = "Ayesha eman"
# message = "Would you like to go out on a date?"
  
  
        
# print(f"Hello {name.title()}, {message}")
# print(name.lower())
# print(name.upper())
# print(name.title())

# famousPerson = "Ghost"
# famousQuote = "\"Choices are consequences\""
# print(f"{famousPerson} once said, {famousQuote}")

# name = " \n \t       Vyrat\nKholi      "
# print(name.rstrip())

