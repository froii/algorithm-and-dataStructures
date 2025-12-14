# Гібридний алгоритм Rabin-Karp + Boyer-Moore
# Основна ідея: поєднуємо переваги обох алгоритмів
# - Від Rabin-Karp: швидке порівняння через хеші
# - Від Boyer-Moore: розумні зсуви при невідповідності

# Приклад використання:
# text = "HELLO WORLD HELLO"
# pattern = "HELLO"
#
# Покрокова робота:
# Крок 1: Обчислюємо хеш pattern "HELLO" = 150 (приклад)
#         Будуємо таблицю зсувів Boyer-Moore
#
# Крок 2: Вікно на позиції 0-4 "HELLO"
#   Хеш "HELLO" = 150 == 150 ✓
#   Додаткова перевірка: "HELLO" == "HELLO" ✓
#   ЗНАЙДЕНО на позиції 0!
#
# Крок 3: Зсув за Boyer-Moore (швидкий пропуск)
#   Вікно на позиції 12-16 "HELLO"
#   Хеш = 150 == 150 ✓
#   "HELLO" == "HELLO" ✓
#   ЗНАЙДЕНО на позиції 12!
#
# Перевага: немає =(


def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def hybrid_search(text, pattern):
    """
    Гібридний алгоритм: Rabin-Karp + Boyer-Moore.
    Використовує хешування для швидкого порівняння та таблицю зсувів для оптимізації.

    Args:
        text: текст для пошуку
        pattern: підрядок для пошуку

    Returns:
        позиція першого входження або -1
    """
    if not pattern or not text:
        return -1

    pattern_length = len(pattern)
    text_length = len(text)

    if pattern_length > text_length:
        return -1

    # Підготовка: обчислюємо хеш патерну та таблицю зсувів
    base = 256
    modulus = 101
    pattern_hash = polynomial_hash(pattern, base, modulus)
    shift_table = build_shift_table(pattern)

    i = 0  # Поточна позиція в тексті

    while i <= text_length - pattern_length:
        # Обчислюємо хеш поточного вікна
        window = text[i:i + pattern_length]
        window_hash = polynomial_hash(window, base, modulus)

        # Якщо хеші співпадають, робимо додаткову перевірку
        if window_hash == pattern_hash:
            # Порівнюємо символи від кінця (як у Boyer-Moore)
            j = pattern_length - 1
            while j >= 0 and text[i + j] == pattern[j]:
                j -= 1

            # Якщо весь патерн співпав
            if j < 0:
                return i  # Знайдено!

        # Використовуємо таблицю зсувів Boyer-Moore для оптимального зсуву
        # Дивимося на символ, що відповідає останньому символу патерну
        if i + pattern_length < text_length:
            shift_char = text[i + pattern_length - 1]
            shift = shift_table.get(shift_char, pattern_length)
        else:
            shift = 1

        i += max(1, shift)  # Робимо зсув (мінімум на 1)

    return -1  # Патерн не знайдено


def hybrid_search_optimized(text, pattern):
    """
    Оптимізована версія гібридного алгоритму з rolling hash.
    Використовує ковзне вікно для швидкого перерахунку хешу.

    Args:
        text: текст для пошуку
        pattern: підрядок для пошуку

    Returns:
        позиція першого входження або -1
    """
    if not pattern or not text:
        return -1

    pattern_length = len(pattern)
    text_length = len(text)

    if pattern_length > text_length:
        return -1

    base = 256
    modulus = 101

    # Обчислюємо хеш патерну та першого вікна
    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_hash = polynomial_hash(text[:pattern_length], base, modulus)
    shift_table = build_shift_table(pattern)
    h_multiplier = pow(base, pattern_length - 1) % modulus

    i = 0

    while i <= text_length - pattern_length:
        # Перевіряємо хеш
        if current_hash == pattern_hash:
            # Порівняння від кінця (Boyer-Moore style)
            j = pattern_length - 1
            while j >= 0 and text[i + j] == pattern[j]:
                j -= 1

            if j < 0:
                return i  # Знайдено!

        # Визначаємо зсув за Boyer-Moore
        if i + pattern_length < text_length:
            shift_char = text[i + pattern_length - 1]
            shift = shift_table.get(shift_char, pattern_length)
        else:
            shift = 1

        # Перераховуємо хеш для нової позиції (rolling hash)
        if i + shift + pattern_length <= text_length:
            # Якщо зсув = 1, використовуємо rolling hash
            if shift == 1 and i + pattern_length < text_length:
                current_hash = (current_hash - ord(text[i]) * h_multiplier) % modulus
                current_hash = (current_hash * base + ord(text[i + pattern_length])) % modulus
                if current_hash < 0:
                    current_hash += modulus
            else:
                # Для великих зсувів перераховуємо хеш з нуля
                current_hash = polynomial_hash(text[i + shift:i + shift + pattern_length], base, modulus)

        i += max(1, shift)

    return -1
