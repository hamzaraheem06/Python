import time as t
import random

# note: bubble sort algorithm

    #1.  Go through the array, one value at a time.
    #2.  For each value, compare the value with the next value.
    #3.  If the value is higher than the next one, swap the values so that the highest value comes last.
    #4.  Go through the array as many times as there are values in the array.


def bubble_sort(nums: list[int]) -> list[int]:
    num_list = nums[:] # copying the list
    for i in range(0, len(num_list)):
        swapped = False
        for j in range(0, len(num_list) - i - 1):
            if num_list[j] > num_list[j+1]: #preceding number greater than proceding number, swap 
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j] # swapping
                swapped = True
        if not swapped: # no swapping mean list is sorted
            break
    
    return num_list

nums = [random.randint(-10**2, 10**2) for _ in range(100_000)]

start_time = t.time_ns()

sorted_nums = bubble_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000) 
# approxmiate 11.733470575 minutes for 100,000 numbers
# average (5 tries) of 8.05819304 seconds for 1,000 numbers.
