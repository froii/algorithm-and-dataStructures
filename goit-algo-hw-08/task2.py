import heapq

print("=" * 70)
print("ДЕМОНСТРАЦІЯ: heapq.heapify(), heappop(), heapreplace()")
print("=" * 70)

# Створюємо масив та перетворюємо у купу
numbers = [15, 10, 25, 8, 30, 5, 12, 20]
print(f"\nПочатковий масив: {numbers}")
heapq.heapify(numbers)
print(f"Після heapify():  {numbers}  ← мінімум (5) на позиції [0]\n")

# heappop - видаляє мінімум
min_val = heapq.heappop(numbers)
print(f"heappop():        {numbers}  ← видалено {min_val}, новий мінімум: {numbers[0]}\n")

# heapreplace - видаляє мінімум та додає новий елемент
old = heapq.heapreplace(numbers, 18)
print(f"heapreplace(18):  {numbers}  ← видалено {old}, додано 18\n")

print("=" * 70)
print("ЧЕРГА З ПРІОРИТЕТАМИ")
print("=" * 70)


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0  # Для збереження порядку при однакових пріоритетах

    def add(self, user, priority):
        # Кортеж: (пріоритет, лічильник, ім'я) - купа сортує за пріоритетом
        heapq.heappush(self.heap, (priority, self.counter, user))
        self.counter += 1
        print(f"+ {user} (пріоритет {priority})")

    def process(self):
        if not self.heap:
            return None
        priority, counter, user = heapq.heappop(self.heap)
        print(f"→ Обробляємо: {user} (пріоритет {priority})")
        return user

    def update_priority(self, user, new_priority):
        # Знаходимо та видаляємо користувача
        for i, (priority, counter, name) in enumerate(self.heap):
            if name == user:
                print(f"🔄 {user}: пріоритет {priority} → {new_priority}")
                self.heap.pop(i)
                heapq.heapify(self.heap)  # Відновлюємо купу
                break
        # Додаємо з новим пріоритетом
        heapq.heappush(self.heap, (new_priority, self.counter, user))
        self.counter += 1

    def show(self):
        print(f"\nЧерга ({len(self.heap)} запитів):")
        # Купа вже відсортована! Показуємо як є
        for priority, counter, user in self.heap:
            p = {1: "🔴 Високий", 2: "🟡 Середній", 3: "🟢 Низький"}[priority]
            print(f"  {user:<15} {p:<15} порядок: {counter}")


# ТЕСТ: Черга з пріоритетами
print("\n1️⃣ Додавання користувачів:")
queue = PriorityQueue()
queue.add("Alice", 2)
queue.add("Bob", 1)
queue.add("Charlie", 3)
queue.add("Diana", 2)
queue.add("Eve", 1)
queue.show()

print("\n2️⃣ Однакові пріоритети - зберігається порядок додавання:")
queue.add("Frank", 2)
queue.add("Grace", 1)
queue.show()

print("\n3️⃣ Обробка запитів (від вищого пріоритету):")
for _ in range(3):
    queue.process()
queue.show()

print("\n4️⃣ Оновлення пріоритету Charlie: 3 → 1")
queue.update_priority("Charlie", 1)
queue.show()

print("\n5️⃣ Обробка всіх запитів:")
while len(queue.heap) > 0:
    queue.process()

print("\n" + "=" * 70)
print("ВИСНОВКИ:")
print("=" * 70)
print("✅ Купа тримає найвищий пріоритет (найменше число) на вершині")
print("✅ При однакових пріоритетах: FIFO (завдяки counter)")
print("✅ Складність: додавання/видалення O(log n), оновлення O(n)")
