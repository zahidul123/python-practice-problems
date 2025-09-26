 ### Problem-4: Validate Email Format
#Write a function that validates emails during user registration.
#-   **Input**: `"test@domain.com"`
#-   **Output**: `True`
#-   **Hint**: Use regular expressions.

import re
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test cases
print(is_valid_email("rest@gmail.com,"))

