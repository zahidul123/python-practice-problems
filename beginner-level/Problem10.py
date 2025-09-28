### Problem-10: Check if a Number is Prime
# Write a function to check if a number is prime, useful in some encryption schemes.   
# -   **Input**: `29`  
#-   **Output**: `True`    
#-   **Hint**: Check divisibility from 2 to `sqrt(n)`.

import math

def is_prime_number(number):
    if number < 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    root_number = int(math.sqrt(number))

    for i in range(3, root_number + 1, 2):
        if number % i == 0:
            return False
    
    return True

print(is_prime_number(29))  
print(is_prime_number(15))  
print(is_prime_number(2))
print(is_prime_number(19))
print(is_prime_number(21))