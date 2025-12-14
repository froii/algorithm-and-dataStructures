# Алгоритм Кнута - Морріса - Пратта(КМП) — це ефективний алгоритм пошуку підрядка в рядку, що працює за лінійний час.

# Основна ідея алгоритму полягає в тому, щоб уникнути повторних порівнянь
# символів, використовуючи інформацію про вже перевірені символи. Для
# цього ми будуємо таблицю lps (longest prefix which is also suffix), яка
# допомагає визначити, на скільки позицій можна зсунути підрядок при
# невідповідності.

# Приклад використання:
# main_string = "ababcababcabc"
# pattern = "abc"
#
# Покрокова робота алгоритму:
# Крок 1: Будуємо LPS таблицю для pattern "abc" → [0, 0, 0]
# Крок 2: Починаємо пошук з позиції 0
#   i=0, j=0: 'a' == 'a' ✓ → переходимо далі
#   i=1, j=1: 'b' == 'b' ✓ → переходимо далі
#   i=2, j=2: 'a' != 'c' ✗ → зсув за LPS, j=0
#   i=2, j=0: 'a' == 'a' ✓ → переходимо далі
#   i=3, j=1: 'b' == 'b' ✓ → переходимо далі
#   i=4, j=2: 'c' == 'c' ✓ → ЗНАЙДЕНО на позиції 2
# Результат: pattern знайдено на індексі 2


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено
