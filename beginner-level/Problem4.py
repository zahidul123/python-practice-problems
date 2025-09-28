### Problem-4: Check if a Word is a Palindrome
# Write a function that checks if a word or phrase is the same when reversed, ignoring spaces and punctuation.
#-   **Input**: `"Madam"`
#-   **Output**: `True`
#-   **Hint**: Normalize the string and compare it to its reverse.

def is_palindrome(input_string):
    left_side = 0
    right_side = len(input_string) - 1
    input_string = input_string.lower()
    while left_side < right_side:
        if input_string[left_side] != input_string[right_side]:
            return False
        left_side += 1
        right_side -= 1
    return True
print(is_palindrome("Madam"))  # True
print(is_palindrome("mm")) 
print(is_palindrome("oooomooo"))  # False
print(is_palindrome("oooo"))  