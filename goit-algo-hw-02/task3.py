"""
Завдання 3 (необов'язкове завдання):
Завдання є додатковим, тому не оцінюється, проте, за бажанням, ви можете отримати конструктивний зворотний зв'язок від ментора.
"""

# Приклад очікуваного результату:
# ( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
# ( 23 ( 2 - 3);: Несиметрично
# ( 11 }: Несиметрично  

signs = {")": "(", "]": "[", "}": "{"}
examples = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]


def check_brackets(text: str) -> bool:
    opener_sign = set(signs.values())
    stack = []

    for s in text:
        if s in opener_sign:
            stack.append(s)
        elif s in signs:
            if len(stack) > 0 and stack[-1] == signs[s]:
                stack.pop()
            else:
                return False

    return not stack



for ex in examples:
    res = check_brackets(ex)
    print(f"{ex}: {'Симетрично' if res else 'Несиметрично'}")
