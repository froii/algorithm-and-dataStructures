

def sort_func(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = sort_func(arr[:mid])
    right = sort_func(arr[mid:])

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# якщо поточна більша - то міняєм мясцями і продовжуємо
# Якщо елемент на позиції j більший, ніж елемент на позиції j + 1, ми міняємо їх місцями. Процес продовжується, поки ми не пройдемо весь список без необхідності в перестановці місцями.
def sort_buble(arr):
    n = len(arr)
    if n < 2:
        return arr

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
