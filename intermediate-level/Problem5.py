### Problem-5: Fibonacci Using Memoization
#Optimize a recursive Fibonacci function using caching, useful in DP-based ML solutions.
#-   **Input**: `50`   
#-   **Output**: `12586269025`
#-   **Hint**: Use `@lru_cache` from `functools`.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test case
print(fibonacci(50))  # Output: 12586269025

# Create a function that take a number and print fibonacci series up to that number
def fibonacci_series(n: int):
    series = [fibonacci(i) for i in range(n)]
    return series
print(fibonacci_series(5)) 