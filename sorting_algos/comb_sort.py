import random 
import time as t

# note: comb sort algorithm
# compare each element with the element that is _gap_ away from it. 
# loop will be from 0 to lenght - gap ( the inner loop)
# outer loop will check if the swapping is occuring or not, as well as gap. if both the condition get false at the same time, the looop terminates.

def comb_sort(nums: list[int]) -> list[int]:
    # Create a copy to avoid modifying the input list
    num_list = nums[:]
    n = len(num_list)
    
    # Initialize gap as the length of the list
    gap = n
    shrink_factor = 1.3  # Optimal shrink factor
    swapped = False
    
    # Continue until gap is 1 and no swaps occur
    while gap > 1 or swapped: # only terminates when both conditions are false.
        # Shrink the gap
        gap = max(1, int(gap / shrink_factor))
        swapped = False
        
        # Compare and swap elements separated by gap
        for i in range(0, n - gap):
            if num_list[i] > num_list[i + gap]: # compare i'th with (i + gap)'th 
                num_list[i], num_list[i + gap] = num_list[i + gap], num_list[i]
                swapped = True # means swapping has occured
    
    return num_list

nums = [random.randint(-10**6, 10**6) for _ in range(1_00_000)]

start_time = t.time_ns()

sorted_nums = comb_sort(nums)

stop_time = t.time_ns()

total_time = stop_time - start_time
print("Time taken (s):", total_time / 1_000_000_000) 
