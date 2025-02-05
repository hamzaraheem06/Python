
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j+1] <  arr[j]:
                arr[j+1] = arr[j+1] + arr[j]
                arr[j] = arr[j+1] - arr[j]
                arr[j+1] = arr[j+1] - arr[j]
                swapped = True
        if not swapped : return
        
numbers = [12, 34, 1, 53, 63, 12, -12]

bubble_sort(numbers)

def square(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("*", end=" ")
        print("\n")

# square(5)

def leftTriangle(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\n")

# leftTriangle(5)

def rightTriangle(n):
    for i in range(1, n+1):
        for j in range(1, n - i + 1):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end="")
        print("\n")


balance = 10.0 

order  = 10

def calc_rem_balance(balance, order):
    try:
        return float(balance) - float(order)
    except:
        return float(balance) - 0.0
    finally:
        print("The calcuations have been done.")

print(calc_rem_balance(balance, order))