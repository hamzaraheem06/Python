import random
import time as t

# note: insertion sort algorithm

    #1.  Take the first value from the unsorted part of the array.
    #2.  Move the value into the correct place in the sorted part of the array.
    #3.  Go through the unsorted part of the array again as many times as there are values.

def insertion_sort(nums: list[int]) -> list[int]:
    num_list = nums[:]

    for i in range(1, len(num_list)):
        j = i
        while j > 0 and num_list[j] < num_list[j - 1]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j - 1]
            j -= 1

    return num_list
        
nums = [random.randint(-10**2, 10**2) for _ in range(100_000)]

start_time = t.time_ns()

sorted_nums = insertion_sort(nums)

stop_time = t.time_ns()


total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000) 

# 9.2980107067 for 100,000 numbers