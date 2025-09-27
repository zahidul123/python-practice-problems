### Problem-9: Password Validator (Security Utility)
# Build a validator that checks for minimum length, uppercase, lowercase, number, and special character.
#-   **Hint**: Use regex or manual checks with `any()`.

import re

def is_valid_password(password: str) -> bool:
   re_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,16}$'
   if not re.match(re_pattern, password):
       return False
   else:
       return True

# Test cases
test_passwords = ["Password123!", "pass", "PASSWORD123!", "Password", "Password123", "Password!"]
for pwd in test_passwords:
    print(f"'{pwd}': {'Valid' if is_valid_password(pwd) else 'Invalid'}")



#another way without regex
def is_valid_password_manual(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in '!@#$%^&*(),.?":{}|<>' for c in password):
        return False
    return True

# Test cases
for pwd in test_passwords:
    print(f"'{pwd}': {'Valid' if is_valid_password_manual(pwd) else 'Invalid'}")


