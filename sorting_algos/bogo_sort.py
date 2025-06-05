import random as r
import time as t

# note: bogo sort algorithm

# 1. Check if the list is sorted.
# 2. If sorted, stop.
# 3. If not sorted, shuffle the list randomly.
# 4. Repeat from step 1.

def bogo_sort(nums: list[int]) -> list[int]:
    num_list = nums[:]

    while not is_sorted(num_list):
        r.shuffle(num_list)
    
    return num_list


def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

nums = [r.randint(-10**2, 10**2) for _ in range(20)]


start_time = t.time_ns()

sorted_nums = bogo_sort(nums)

stop_time = t.time_ns()

print("Unsorted:", nums)
print("Sorted:",sorted_nums)

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000)

# umm what da fuq??? can't even sort 20 numbers. stubid algorithm. took 1.81s to sort 10 numbers, and undefined time for 20 stupidddd, bro it is still going on after 10 minsssssss. 