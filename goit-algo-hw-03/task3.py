"""Переміщує n дисків з source на target через auxiliary"""
# hanoi(A→C, n=3)
# ├─ hanoi(A→B, n=2)[Крок 1: звільнити верхні 2]
# │  ├─ hanoi(A→C, n=1) → move 1
# │  ├─ move 2 (A→B)
# │  └─ hanoi(C→B, n=1) → move 1
# ├─ move 3 (A→C)[Крок 2: найбільший на місце]
# └─ hanoi(B→C, n=2)[Крок 3: повернути 2 диски]
# ├─ hanoi(B→A, n=1) → move 1
# ├─ move 2 (B→C)
# └─ hanoi(A→C, n=1) → move 1


def print_towers(state):
    """Малює вежі вертикально"""
    max_height = max(len(state['A']), len(state['B']), len(state['C']))

    for level in range(max_height - 1, -1, -1):
        line = ""
        for rod in ['A', 'B', 'C']:
            if level < len(state[rod]):
                disk = state[rod][level]
                line += f" {'█' * disk} ".center(10)
            else:
                line += " | ".center(10)
        print(line)

    print("-" * 30)
    print("   A          B          C   ")
    print()


def move_disk(state, source, target):
    disk = state[source].pop()
    state[target].append(disk)
    print(f"\nПеремістити диск {disk} з {source} на {target}")
    print_towers(state)

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
