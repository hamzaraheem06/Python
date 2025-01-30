# 1. check if the number is prime or not

def isPrime(a: int): # typescript mentioned ????

    if a == 0 or a == 1: return False

    for i in range(2, int(a/2) + 1): # adding 1 because the stop value is not included in the loop iteration
        if a % i == 0: # if a gets divided by any number upto its half, it is not a prime number. The condition is upto half because no number is divisible by more than its half.
            return False
    return True

# num = int(input("Enter a number: "))
# print("Prime" if isPrime(num) else "Not prime")

# 2. Print prime numbers till n

def sumOfPrime(a: int):
    sum = 0 # initializing sum to 0
    for i in range(2, a + 1): # checking all the integers upto entered number.
        if isPrime(i): 
            sum+=i # adding the prime instances.

    return sum

# num = int(input("Enter a number: "))
# print(f"The sum of prime numbers till {num} is {sumOfPrime(num)}")

def factorial(a: int):
    if a < 0:
        raise ValueError("Factorial is not defined for negative values.")

    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

# 3. count trailing zeros in a factorial of a number

# a trailing zero is the zero which has no non-zero digits on the right. 

# 40320 has one trailing zero. the other zero is not trailing zero becuase it has a non-zero value on the right.
def calcTrailingZeros(fact: int): 
    count = 0
    while fact % 10 == 0: # since the % return the last digit in the number, we are checking if that digit is zero. if that is zero, we increment the counter and remove that last digit by dividing by zero to move furthur. As soon as the last digit is a non-zero value the loop breaks and we get the number of trailing zeros.
        count += 1 # increasing the counter 
        fact //= 10 # slicing the factorial value one by one
    return count

# num = int(input("Enter a number: "))
# fact = factorial(num)
# print("The factorial is", fact)
# print(f"The factorial of {num} is {fact} and number of trailing zeros are {calcTrailingZeros(fact)}") 

# The upper solution is based on the value of factorial of a number. This is not very good because the value of factorial increase exponentially as the integer value increase by only 1

# To create a memory and time efficient solution we work on the actual integer and not its factorial


def findTrailingZeros(num: int):
    if num < 0: # factorial is not defined for negative values
        return -1
    
    count = 0 # to count the # of trailing zeros
    divisor = 5 # each multiple of 5 contributes as one trailing zero, 
    # so dividing by five will give us no of trailing zeros. however for bigger integers there will be more trailing zeros so we divide by 25 which will contribute the remaining trailing zeros. and for even larger numbers, we divide by 125, and so on.

    # so the idea becomes #of trailing zeros = floor(num/5) + floor(num/25) + floor(num/125) + ......

    while num >= divisor:  # if the divisor become larger than the num, then floor(num/divisor) will be zero i.e. there are no remaining trailing zeros, so the loop breaks.
        count += num // divisor # count + num // divisor 
        divisor*=5

    return count

# ******************* Example
# lets find the number of trailing zeros in 28! using the above logic

# function initialization
    # count = 0     divisor = 5
    # 28 >= 5 is true so the condition becomes true 
    # so count becomes floor(28/5) = 5

    # count = 5     divisor = 25
    # 28 >= 25 is true 
    # count = 5 + floor(28/25) = 5 + 1 = 6

    # count = 6       divisor = 125

    # 28 >= 125 becomes false and we get our answer


# num = int(input("Enter a number: "))
# print(f"The number of trailing zeros in factorial of {num} i.e. {factorial(num)} are {findTrailingZeros(num)}")

# very good solution 👍👍

# Sum of digits of a Number till it Becomes a Single digit.

# sum individual digits one by one of a number using the modulo operator and then discard the added term.
# check if the resulting sum is a single digit number.

def sum_of_digits_of_num(num: int):
    while True:
        sum = 0
        while num > 0: 
            sum += num % 10 # since % 10 returns the last digit in a number we add it to the sum 
            num //= 10 # using floor operator because division will be floating value which causes a logical error in the program 

        if 0 < sum < 10: 
            return sum
        
        num = sum


# num = int(input("Enter a number: "))
# print(f"Sum of digits of {num} is {sum_of_digits_of_num(num)}")

# palindrome_integer
# a palindrome integer is an integer that remains same even after the reversing it.

# reverse the number and compare with the original number.

def palindrome_integer(num: int) -> bool:
    temp = num
    reversed = 0
    while temp > 0:
        reversed = (reversed * 10 ) + temp % 10
        temp //= 10

    if reversed == num:
        return True
    else:
        return False

# num = int(input("Enter a number: "))

# print("Palindrome" if palindrome_integer(num) else "Not Palindrome")

# Armstrong Number
# an armstrong number is a number whose sum of digits each raised to power number of digits in the number is equal to the orginal number.

# calc the number of digits len_digits in the number
# using modulo operator sum all the digits raised to len_digits and discard the last digit after its sum has been calculated.

def is_armstrong(a: int) -> bool:
    len_of_number = len(str(a)) # calculating the # of digits in the number

    temp = a # creating a temp var for manipulation
    sum = 0 # initializing the sum value
    while temp != 0:
        sum += ( temp % 10 ) ** len_of_number # seperating each digit one-by-one and add their power to the sum var.
        temp //= 10 # discard the added term.
    
    return True if sum == a else False  # comparing the values

# Perfect number

# An integer is a perfect number if it is equal to sum of its proper divisors.

# initialize a sum var to 1, because one is a proper divisor of every number.
# run a loop from 2 to half of the number 
# check if the i divides the number completely if yes add it to sum 
# compare the values

def is_perfect(a: int) -> bool: # very self explainable code.
    sum = 1
    for i in range(2, a // 2 + 1):
        if not a % i:
            sum += i
    
    return True if sum == a else False  # comparing the values

# prime factors are numbers that divide the number completely and they are prime. 

# intialize an empty list to store the prime factors.
# a number can only be divisible by a number less than or equal to half of the number.
# we check if the i divides the number and if it is also a prime number
# we append i the number of times it divides the number, and after each appending we remove its factor from the original value


def prime_factors(a: int) -> list:
    factors = []

    for i in range(2, a // 2 + 1):
        while  not a % i and isPrime(i):
            factors.append(i)
            a //= i

    return factors

print(prime_factors(90))
    

