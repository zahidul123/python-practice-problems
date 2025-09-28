### Problem-8: Factorial Using Recursion
# Write a function to return the factorial of a number, used in data science combinations calculation.
# -   **Input**: `5`   
# -   **Output**: `120`   
# -   **Hint**: Base case is `0! = 1`, then recurse.

def recursive_factorial(number):
    if number == 0:
        return 1
    else:
        return number * recursive_factorial(number - 1)
print(recursive_factorial(5))
print(recursive_factorial(0))