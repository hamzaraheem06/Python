


# maximum in a list
def max_algo(num_list):
    maximum_num = num_list[0]
    for i in range(2, len(num_list)):
        if num_list[i] > maximum_num:
            maximum_num = num_list[i]
    return maximum_num

# searching for a value one by one through a list
def linear_search(num_list, key):
    for i in range(0, len(num_list)):
        if num_list[i] == key:
            return i
    return -1


def binary_search(values_list, value):
    low = 0
    high = len(values_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Floor division
        if values_list[mid] == value:
            return mid
        elif values_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1

numbers_list = [21, 34, 34, 12, 234, 12]
numbers_list.sort();
print(numbers_list)
target = 12

print(binary_search(numbers_list, 14))
