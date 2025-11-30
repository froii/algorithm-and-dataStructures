from functools import lru_cache

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value


if __name__ == "__main__":
    n = 10  # Example input
    print(f"Fibonacci of {n} using lru_cache: {fibonacci(n)}")
    print(f"Fibonacci of {n} using manual memoization: {fibonacci_memo(n)}")