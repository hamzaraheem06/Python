# while condition:
    # statements 

i = 0

while i < 3:
    print("Sniper ", i)
    i+=1

# unfortunately we dont have 

# like we have to explicitly create a variable to control the while loop as in other language, same is the case in python. 

# for has two overloads 
# i) for i in seq: this is similar foreach loop in many programming languages.

# for i in [12, 34, 12, 1]:
#     print(i)

# 12
# 34
# 12
# 1

# ii) for i in range(start, stop, step):
    # statements 
# this is the conventional for loop as we use in many languages 

# comparison with C++
# for(int i = initial; i < stop; i update/ step) 

# Note: if you dont want to use the controlling variable in the body of the loop, you can just write _ in place of the variable, indicating that this is used to just run the loop but has no value in the statement 

for _ in range(0, 5):
    print("Sniper ")

# Sniper 
# Sniper 
# Sniper 
# Sniper 
# Sniper 



