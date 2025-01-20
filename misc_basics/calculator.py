# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# operator = input("What operation do you want to perform? ")
#
# if operator == '+':
#     print(x+y)
# elif operator == '-':
#     print(x-y)
# elif operator == '*':
#     print(x*y)
# elif operator == '/':
#     print(x / y)
# elif operator == '%':
#     print(x%y)
# elif operator == '**':
#     print(x ** y)
# else:
#     print("Invalid operator")

# def iseven(num):
#     return num % 2 == 0
#
# for i in range(1, 21):
#     print("Even" if iseven(i) else "Odd")
#
# x = 12
#
#
# # print("Even" if i % 2 == 0 else "Odd")


# Bubble sort in python
# numList = [1, 23, 12, 35, -34]
#
# for i in range(0, len(numList) - 1):
#     swapped = False
#     for j in range(0, len(numList) - 1):
#         if numList[j] > numList[j+1] :
#             numList[j] = numList[j] + numList[j+1]
#             numList[j+1] = numList[j] - numList[j+1]
#             numList[j] = numList[j] - numList[j+1]
#             swapped = True
#     if not swapped:
#         break
#
# for i in numList:
#     print(f"{i} ", end="")

# Binary search

numList = [1, 23, 12, 35, -34]
key = 12

def binarysearch(numbers, value):
    numbers.sort()
    low = 0
    high = len(numbers) - 1
    while high>=low:
        mid = int( (low + high) / 2)
        if numbers[mid] == value:
            return mid
        elif value > numbers[mid]:
            low = mid + 1
            continue
        else:
            high = mid - 1
            continue
    return -1

indexOfKey = binarysearch(numList, key)

print(f"{key} is at index {indexOfKey} of {numList} \nNote: If index is -1, the key is not present in the list")










