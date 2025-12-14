# Алгоритм Aho-Corasick — алгоритм пошуку МНОЖИНИ підрядків одночасно.
# Основна ідея: будуємо автомат (trie + failure links), який дозволяє знайти всі
# входження всіх патернів за ОДИН прохід по тексту.
# для антивірус - сканування 100,000 + сигнатур

# Приклад використання:
# text = "ABABCABCD"
# patterns = ["ABC", "AB", "BC"]
#
# Покрокова робота:
# Крок 1: Будуємо trie з patterns
#        root
#       /    \
#      A      B
#     /        \
#    B          C
#   / \
#  [AB] C
#      /
#    [ABC]
#
# Крок 2: Додаємо failure links (для швидкого переходу при невдачі)
#
# Крок 3: Проходимо текст "ABABCABCD"
#   Позиція 0-1: знайдено "AB" ✓
#   Позиція 0-2: знайдено "ABC" ✓
#   Позиція 1-2: знайдено "BC" ✓
#   Позиція 4-5: знайдено "AB" ✓
#   Позиція 4-6: знайдено "ABC" ✓
#
# Результат: знайдено всі входження всіх патернів за O(n + m + z)
# де n - довжина тексту, m - сума довжин патернів, z - кількість знайдених входжень


class AhoCorasickNode:
    """Вузол для дерева (trie) алгоритму Aho-Corasick."""

    def __init__(self):
        self.children = {}  # Словник дочірніх вузлів
        self.fail = None    # Failure link
        self.output = []    # Список знайдених патернів у цьому вузлі


class AhoCorasick:
    """Реалізація алгоритму Aho-Corasick для пошуку множини підрядків."""

    def __init__(self, patterns):
        """
        Ініціалізація з набором патернів.

        Args:
            patterns: список підрядків для пошуку
        """
        self.root = AhoCorasickNode()
        self.patterns = patterns
        self._build_trie()
        self._build_failure_links()

    def _build_trie(self):
        """Будуємо trie з усіх патернів."""
        for pattern_idx, pattern in enumerate(self.patterns):
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = AhoCorasickNode()
                node = node.children[char]
            # Відмічаємо кінець патерну
            node.output.append((pattern_idx, pattern))

    def _build_failure_links(self):
        """Будуємо failure links для ефективної навігації."""
        from collections import deque

        queue = deque()

        # Ініціалізуємо failure links для дітей root
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        # BFS для побудови failure links
        while queue:
            current = queue.popleft()

            for char, child in current.children.items():
                queue.append(child)

                # Шукаємо failure link
                fail_node = current.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail

                child.fail = fail_node.children[char] if fail_node else self.root

                # Додаємо output від failure link
                child.output.extend(child.fail.output)

    def search(self, text):
        """
        Шукає всі входження всіх патернів у тексті.

        Args:
            text: текст для пошуку

        Returns:
            список кортежів (позиція, індекс_патерну, патерн)
        """
        results = []
        node = self.root

        for i, char in enumerate(text):
            # Переходимо по failure links, поки не знайдемо збіг або root
            while node and char not in node.children:
                node = node.fail

            if not node:
                node = self.root
                continue

            node = node.children[char]

            # Додаємо всі знайдені патерни в цій позиції
            for pattern_idx, pattern in node.output:
                start_pos = i - len(pattern) + 1
                results.append((start_pos, pattern_idx, pattern))

        return results


def aho_corasick_search(text, pattern):
    """
    Адаптер для використання в тестуванні (пошук одного патерну).
    Повертає позицію першого входження або -1.

    Args:
        text: текст для пошуку
        pattern: підрядок для пошуку

    Returns:
        позиція першого входження або -1
    """
    ac = AhoCorasick([pattern])
    results = ac.search(text)

    if results:
        return results[0][0]  # Повертаємо позицію першого знайденого входження
    return -1


def aho_corasick_search_multiple(text, patterns):
    """
    Пошук множини патернів одночасно.

    Args:
        text: текст для пошуку
        patterns: список підрядків для пошуку

    Returns:
        список кортежів (позиція, індекс_патерну, патерн)
    """
    ac = AhoCorasick(patterns)
    return ac.search(text)
