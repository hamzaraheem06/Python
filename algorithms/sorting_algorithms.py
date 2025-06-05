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

def insertion_sort(nums: list[int]) -> list[int]:
    num_list = nums[:]

    for i in range(1, len(num_list)):
        j = i
        while j > 0 and num_list[j] < num_list[j - 1]:
            num_list[j-1], num_list[j] = num_list[j], num_list[j - 1]
            j -= 1

    return num_list

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
    # sorted_indices = [nums[i] for num in num_list for i, norm in enumerate(normalized_nums) if norm == num]
    # return sorted_indices

    return num_list # Returns sorted normalized values

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
 