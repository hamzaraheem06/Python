
# note: bucket sort algorithm 

# note: Bucket sort is best for floating-point numbers in [0, 1).

# Create n empty buckets (Or lists) and do the following for every array element arr[i].

#    1. Insert arr[i] into bucket[n*array[i]]
#    2. Sort individual buckets using any stable sorting algorithm, preferablly insertion sort.
#    3. Concatenate all sorted buckets.

from sorting_algorithms import insertion_sort
import time as t
import random

def bucket_sort(nums: list[float]) -> list[float]:
    n = len(nums)

    buckets = [[] for _ in range(n)]

    for num in nums:
        index = int(num * n)
        buckets[index].append(num) 

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    num_list = []
    
    for bucket in buckets:
        num_list.extend(bucket)
    
    return num_list


def bucket_sort_normalized(nums: list[int]) -> list[int]:
    
    min_value, max_value = min(nums), max(nums)

    if max_value == min_value:
        return nums[:]  # Already sorted if all values are the same

    normalized_nums = [(x - min_value) / (max_value - min_value) for x in nums]

    n = len(normalized_nums)
    
    buckets = [[] for _ in range(n)]

    for num in normalized_nums:
        index = min(int(num * n), n - 1)
        buckets[index].append(num) 

    for i in range(n):
        buckets[i] = insertion_sort(buckets[i])

    num_list = []
    
    for bucket in buckets:
        num_list.extend(bucket)
    
    # Denormalize to original values if needed, or return normalized sorted values
    # If you want original values sorted:
    sorted_indices = [nums[i] for num in num_list for i, norm in enumerate(normalized_nums) if norm == num]
    return sorted_indices

    return num_list # Returns sorted normalized values

nums = [random.random() for _ in range(1_00_000)] # for normal data

# nums = [random.randint(-10**2, 10**2) for _ in range(1_00)] # for unnormal data

start_time = t.time_ns()

sorted_nums = bucket_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000) 

# took 2.6597006 seconds to sort 1,000,000 floating numbers. woww
# the above version of the code is for when the inputs are in between [0, 1)

# note: for inputs outside this range we need to normalize the inputs before we distribute them among the buckets. because the bucket number is decided using the value ->index = int(value * n)

# normalization is as done as below:

# Suppose your numbers are in the range [min_value, max_value].
# To normalize each number x to [0, 1), use:
# normalized_x = (x - min_value) / (max_value - min_value)

    