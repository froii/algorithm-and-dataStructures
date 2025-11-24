"""
Код виконується, використано deque з модуля collections у Python.
Програма перевіряє, чи є заданий рядок паліндромом, враховуючи рядки з парною та непарною кількістю символів, та є нечутливою до регістру та пробілів.
"""

from collections import deque

test_strings = [
    "А роза упала на лапу Азора",
    "Madam",
    "Step on no pets",
    "Not a palindrome",
    "12321",
    "123321",
    "Was it a car or a cat I saw",
]


def is_palindrome(s: str) -> bool:
    try:
        s = "".join(c.lower() for c in s if not c.isspace())
    except Exception:
        return False

    w = deque(s)
    while len(w) > 1:
        if w.popleft() != w.pop():
            return False
    return True


def main():
    for s in test_strings:
        print(f"'{s}' -> {is_palindrome(s)}")


if __name__ == "__main__":
    main()
