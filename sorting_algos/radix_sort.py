import random as r
import time as t

# note: radix sort algorithm 

# note: use when the data list is only positive numbers

#1.  Start with the least significant digit (rightmost digit).
#2.  Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
#3.  Move to the next digit, and sort again, like in the step above, until there are no digits left.

def radix_sort(nums: list[int]) -> list[int]:
    if not nums: # empty list case
        return []

    num_list = nums[:]
    
    # Handle negative numbers (optional, assuming non-negative for now)
    if any(x < 0 for x in num_list):
        raise ValueError("Radix sort requires non-negative integers")

    # Find the maximum number to determine the number of digits
    max_num = max(num_list, default=0)
    n = len(str(max_num)) if max_num > 0 else 1  # At least one digit

    for i in range(n):
        radix_array = [[], [], [], [], [], [], [], [], [], []] # 10 buckets for each decimal digit

        for num in num_list: # distributing the numbers in list
            radix_array[(num // 10**i) % 10].append(num) 

        num_list = [] # emptying the original list 

        for bucket in radix_array: # reinserting the elements in sorted manner
            num_list.extend(bucket) 

    return num_list

nums = [r.randint(0, 10**6) for _ in range(1_000_000)]

start_time = t.time_ns()

sorted_nums = radix_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000)

# myArray = [170, 45, 75, 90, 802, 24, 2, 66]

# print(radix_sort(myArray))