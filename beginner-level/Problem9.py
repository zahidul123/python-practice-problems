### Problem-9: Sum of Digits of an Integer
# For a gamification feature, sum the digits of a user’s ID to generate a unique color code.
#-   **Input**: `9875`    
#-   **Output**: `29`   
#-   **Hint**: Use `//` and `%` or string conversion.

def sum_of_digits(number):
    total = 0
    while number > 0:
        last_digit = number % 10
        total += last_digit
        number = number // 10
    return total

print(sum_of_digits(9875))
print(sum_of_digits(12345))
print(sum_of_digits(0))
