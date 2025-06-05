import random
import time as t

def partition(nums, low, high) -> int:
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
        
    nums[i+1], nums[high] = nums[high], nums[i+1] 

    return i + 1 # pivot point 


def quick_sort(nums: list[int], low = 0, high = None) -> list[int]:
    if high is None:
        high = len(nums) - 1
    
    if low < high:
        partition_index = partition(nums, low, high)
        quick_sort(nums, low, partition_index - 1)
        quick_sort(nums, partition_index + 1, high)
    
    return nums
    
nums = [random.randint(-10**6, 10**6) for _ in range(1_00_000)]

start_time = t.time_ns()

sorted_nums = quick_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000) 
