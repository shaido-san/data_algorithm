def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return ("no")

numbers = [3, 7, 1, 9, 5, 2, 6, 8]
print(linear_search(numbers, 9))
print(linear_search(numbers, 4))