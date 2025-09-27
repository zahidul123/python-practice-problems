### Problem-5: Fibonacci Using Memoization
#Optimize a recursive Fibonacci function using caching, useful in DP-based ML solutions.
#-   **Input**: `50`   
#-   **Output**: `12586269025`
#-   **Hint**: Use `@lru_cache` from `functools`.


#NB: I cannot understand the problem properly but i have thought that you want next fibonacci number after 50
# So i have implement that way

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(50))  # Output: 12586269025
