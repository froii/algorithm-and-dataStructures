import timeit

from algs import (
    aho_corasick_search,
    boyer_moore_search,
    hybrid_search,
    hybrid_search_optimized,
    kmp_search,
    rabin_karp_search,
)


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def benchmark_algorithm(algorithm, text, pattern, number=100):
    time = timeit.timeit(lambda: algorithm(text, pattern), number=number)
    return time


def main():
    try:
        article1 = read_file('text/стаття 1.txt')
        article2 = read_file('text/стаття 2.txt')
    except FileNotFoundError:
        print("Помилка: нема файлів")
        return

    existing_pattern = "алгоритм"
    fake_pattern = "абракадабрахзхзхзневірнийпідрядок"

    algorithms = {
        'Boyer-Moore': boyer_moore_search,
        'Knuth-Morris-Pratt': kmp_search,
        'Rabin-Karp': rabin_karp_search,
        'Aho-Corasick': aho_corasick_search,
        'Hybrid (RK+BM)': hybrid_search,
        'Hybrid Optimized': hybrid_search_optimized
    }

    texts = {
        'Стаття 1': article1,
        'Стаття 2': article2
    }

    patterns = {
        'Існуючий підрядок': existing_pattern,
        'Вигаданий підрядок': fake_pattern
    }

    results = {}

    for text_name, text_content in texts.items():
        results[text_name] = {}
        print(f"\n{'=' * 80}")
        print(f"Назва файлу: {text_name}. Довжина: {len(text_content)} символів\n")
        print(f"{'=' * 80}")

        for pattern_name, pattern in patterns.items():
            results[text_name][pattern_name] = {}
            print(f"\n{'-' * 80}")
            print(f"Підрядок: {pattern_name} ('{pattern[:50]}...' )" if len(
                pattern) > 50 else f"Підрядок: {pattern_name} ('{pattern}')")
            print(f"{'-' * 80}")

            for algo_name, algo_func in algorithms.items():
                time_taken = benchmark_algorithm(algo_func, text_content, pattern, number=100)
                results[text_name][pattern_name][algo_name] = time_taken

                result = algo_func(text_content, pattern)
                found = "✓ Знайдено" if result != -1 else "✗ Не знайдено"

                print(f"{algo_name:25} {time_taken:10.6f} секунд   {found}")

            fastest = min(results[text_name][pattern_name],
                          key=results[text_name][pattern_name].get)
            print(f"\n{'':25} Найшвидший: {fastest}")

    print("\n\n" + "=" * 80)
    print("Рузультати порівняння алгоритмів пошуку підрядка")
    print("=" * 80)

    print("\nСередній час виконання по всіх тестах:")
    avg_times = {}
    for algo_name in algorithms.keys():
        total_time = 0
        count = 0
        for text_name in texts.keys():
            for pattern_name in patterns.keys():
                total_time += results[text_name][pattern_name][algo_name]
                count += 1
        avg_times[algo_name] = total_time / count
        print(f"{algo_name:25} {avg_times[algo_name]:10.6f} секунд")

    fastest_overall = min(avg_times, key=avg_times.get)
    print(f"\nНайшвидший алгоритм в цілому: {fastest_overall}")


if __name__ == "__main__":
    main()
