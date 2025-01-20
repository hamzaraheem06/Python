# define: if statement is used to execute a set of indented lines of code based on a boolean expression

# if expression:
    # statement of if body

# note: the statements indented are evaluated if the boolean expression returns True, if the condition evaluates to False the coresponding indented statements are skipped and the interpreter starts translating from the previously indented level.

# discount = 0

# amount = int(input("Enter order amount: "))

# if amount > 1000:
#     discount = amount * 0.1

# print(f"Your total is: {amount - discount}")

# define: if else is a continuation to if. it allows us to execute one of the two code blocks based on a boolean expression.

# if expression:
    # statements of if body
# else:
    # statements of else body

# note: the statements indented corresponding to if statements are executed if the boolean expression evaluates to True, if the condition is False the else block is exectuted. After execution of either block, the flow continues from the previous indentation level.

# age = int(input("Enter your age: "))

# if age > 18:
#     print("You are eligible to vote.")
# else: 
#     print("You are not eligible to vote.")

# define: if elif else is a further continuation to if else which allows us to execute a code block based on several condition. All the conditions are evaluated sequentially from top to bottom and the coresponding block of the condition which is evaluated to True is executed. If neither of the condition returns a True value, else block is executed. 

# if expression1:
#     statements
# elif expression2:
#     statements
#         .
#         .
#         .
# elif expressionN:
#     statements
# else: 
#     statements

# note: The interpreter starts from the if condition if it is true the corresponding block of statements are executed. if it is False, the interpreter checks the conditon of the following elif and executes it if it evaluates to True. If False the flow toward next condition until it reaches else and execute it if neither of the above expression evaluate to True. 

discount = 0

amount = int(input("Enter your purchase amount: "))

if amount > 10000:
    discount = amount * 0.2
elif 5000 < amount <= 10000:
    discount = amount * 0.1
elif 1000 < amount <= 5000:
    discount = amount * 0.05
else: 
    discount = 0

print(f"Total cost after discount is {amount - discount}")