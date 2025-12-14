def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0
    next_greater = None

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            next_greater = arr[mid]
            right = mid - 1

    return (steps, next_greater)


arr = [1.1, 2.3, 3.5, 4.7, 5.9, 7.1]

print(binary_search_with_upper_bound(arr, 3.5))
print(binary_search_with_upper_bound(arr, 3.6))
print(binary_search_with_upper_bound(arr, 0.5))
print(binary_search_with_upper_bound(arr, 8.0))
print(binary_search_with_upper_bound(arr, 7.1))
print(binary_search_with_upper_bound(arr, 5.0))

arr2 = [10, 15, 18, 20, 25, 28, 30, 35, 38, 40, 45, 48, 50,
        55, 58, 60, 65, 68, 70, 75, 78, 80, 83, 85, 87, 89, 90]
print(binary_search_with_upper_bound(arr2, 55))
print(binary_search_with_upper_bound(arr2, 10))
print(binary_search_with_upper_bound(arr2, 95))
