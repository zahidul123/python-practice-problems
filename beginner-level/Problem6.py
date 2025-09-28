### Problem-6: Capitalize First Letter of Each Word
# Build a custom title formatter that capitalizes the first letter of each word without using `.title()`.
# -   **Input**: `"python for web developers"`
# -   **Output**: `"Python For Web Developers"`
# -   **Hint**: Use `.split()` and loop through each word.

def capitalize_title(input_string):
    splited_words = input_string.lower().split(" ")
    capitalized_words = []
    for word in splited_words:
        
        if word:
            capitalized_word = word[0].upper() + word[1:].lower()
            capitalized_words.append(capitalized_word)
        else:
            capitalized_words.append(word)

    return " ".join(capitalized_words)

print(capitalize_title("python for web developers"))