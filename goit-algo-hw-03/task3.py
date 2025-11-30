"""Переміщує n дисків з source на target через auxiliary"""


def move_disk(state, source, target):
    disk = state[source].pop()
    state[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {state}")


#   hanoi(state, 'A', 'B', 'C',  n)
def hanoi(state, source, auxiliary, target, n):
    if n == 1:
        move_disk(state, source, target)
    else:
        hanoi(state, source, target, auxiliary, n - 1)

        move_disk(state, source, target)

        hanoi(state, auxiliary, source, target, n - 1)


if __name__ == "__main__":
    n = int(input("Надай кількість веж... якщо більше 5 то не гарантую що не впаде)"))
    hanoi_list = list(range(n, 0, -1))

    state = {'A': hanoi_list, 'B': [], 'C': []}

    print(f"Початковий стан: {state}")
    hanoi(state, 'A', 'B', 'C', n)
    print(f"Кінцевий стан: {state}")
