import random
import time as t

#note: selection sort algorithm

    #1.  Go through the array to find the lowest value.
    #2.  Move the lowest value to the front of the unsorted part of the array.
    #3.  Go through the array again as many times as there are values in the array.


def selection_sort(nums: list[int]) -> list[int]:
    num_list = nums[:]
    n = len(num_list)

    for i in range(0, n - 1):
        lowest = i
        for j in range(i+1, n):
            if num_list[j] < num_list[lowest]:
                lowest = j
            
        num_list[i], num_list[lowest] = num_list[lowest], num_list[i]
    
    return num_list

nums = [random.randint(-10**2, 10**2) for _ in range(100_000)]

start_time = t.time_ns()

sorted_nums = selection_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000)

# approxmiate 8.8500373217 minutes for 100,000 numbers
# average (15 tries) of 0.1093792667 seconds for 1,000 numbers.