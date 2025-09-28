### Problem-2: Count Vowels in a Sentence
#As part of a data-cleaning pipeline, count how many vowels are in a string to later analyze readability.
#-   **Input**: `"Data Science is awesome"`
#-   **Output**: `10`
#-   **Hint**: Convert string to lowercase and check each character.

input_string = "Data Science is awesome"
vowels = "aeiou"
count = 0
for letter in input_string.lower():
    if letter in vowels:
        print(letter)
        count += 1
    
print(count)


