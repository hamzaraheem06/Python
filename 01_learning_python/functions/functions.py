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

sum = lambda x, y : x + y

print(sum(12, 23))