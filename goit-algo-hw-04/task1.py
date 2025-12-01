import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def benchmark_algorithms():
    sizes = [100, 1000, 5000, 10000]
    results = []

    for size in sizes:
        random_data = [random.randint(0, 10000) for _ in range(size)]

        if size <= 5000:
            time_insertion = timeit.timeit(
                lambda: insertion_sort(random_data.copy()),
                number=10
            ) / 10
        else:
            time_insertion = None

        time_merge = timeit.timeit(
            lambda: merge_sort(random_data.copy()),
            number=10
        ) / 10

        time_timsort = timeit.timeit(
            lambda: sorted(random_data.copy()),
            number=10
        ) / 10

        results.append({
            'size': size,
            'insertion': time_insertion,
            'merge': time_merge,
            'timsort': time_timsort
        })

    return results


print(f"{'Розмір':<10} {'Insertion Sort':<20} {'Merge Sort':<20} {'Timsort':<20}")
print("-" * 70)

results = benchmark_algorithms()
for r in results:
    insertion_time = f"{r['insertion']:.6f} сек" if r['insertion'] else "N/A (занадто повільно)"
    print(f"{r['size']:<10} {insertion_time:<20} {r['merge']:.6f} сек{'':<7} {r['timsort']:.6f} сек")
