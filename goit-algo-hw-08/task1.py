import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Додає елемент у купу"""
        heapq.heappush(self.heap, value)

    def extract_min(self):
        """Видаляє та повертає мінімальний елемент"""
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def get_min(self):
        """Повертає мінімальний елемент без видалення"""
        if not self.heap:
            return None
        return self.heap[0]

    def __len__(self):
        """Повертає розмір купи"""
        return len(self.heap)


def min_cost(cable_len):
    if not cable_len:
        return 0

    # Перетворюємо список у мінімальну купу (min-heap)
    heapq.heapify(cable_len)
    total_cost = 0

    # Поки є більше одного кабеля для з'єднання
    while len(cable_len) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cable_len)
        second = heapq.heappop(cable_len)
        # З'єднуємо їх (сума довжин)
        union = first + second
        # Додаємо вартість з'єднання до загальної суми
        total_cost += union
        # Повертаємо з'єднаний кабель назад у купу
        heapq.heappush(cable_len, union)

    return total_cost


def merge_k_lists(lists):
    # Купа для зберігання елементів: (значення, індекс_списку, індекс_елемента)
    heap = []
    # Крок 1: Додаємо перший елемент з кожного списку в купу
    for i, lst in enumerate(lists):
        if lst:
            print(f"Додаємо перший елемент зі списку {i}: {lst[0]}")
            heapq.heappush(heap, (lst[0], i, 0))

    # Результуючий відсортований список
    result = []
    print(f"Початковий стан купи: {heap}")
    # Крок 2: Поки купа не порожня
    while heap:
        # Витягуємо найменший елемент з купи
        val, list_idx, elem_idx = heapq.heappop(heap)
        # Додаємо його значення до результату
        result.append(val)
        # Крок 3: Якщо в тому ж списку є наступний елемент
        if elem_idx + 1 < len(lists[list_idx]):
            # Беремо наступний елемент з того ж списку
            next_val = lists[list_idx][elem_idx + 1]
            # Додаємо його в купу з оновленим індексом позиції
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result


# Приклад 1: Мінімальні витрати на з'єднання кабелів
cables = [4, 3, 2, 6]
print("=" * 50)
print("ЗАДАЧА 1: Мінімальні витрати на з'єднання кабелів")
print("=" * 50)
print(f"Довжини кабелів: {cables}")
print(f"Мінімальні витрати: {min_cost(cables)}")
print()

# Приклад 2: Злиття k відсортованих списків
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("=" * 50)
print("ЗАДАЧА 2: Злиття k відсортованих списків")
print("=" * 50)
print(f"Вхідні списки: {lists}")
merged_list = merge_k_lists(lists)
print(f"Відсортований список: {merged_list}")

# Приклад 3: Використання класу MinHeap
print("\n" + "=" * 50)
print("ПРИКЛАД 3: Клас MinHeap")
print("=" * 50)
min_heap = MinHeap()
values = [5, 3, 7, 1, 9, 2]
print(f"Додаємо значення: {values}")
for val in values:
    min_heap.insert(val)

print(f"Мінімальний елемент (без видалення): {min_heap.get_min()}")
print("Видаляємо мінімальні елементи:")
while len(min_heap) > 0:
    print(f"  {min_heap.extract_min()}")
