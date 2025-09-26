### Problem-11: Find the most frequent character in the paragraph

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
char_frequency = {}

for char in rhyme:
    if (ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122): 
    # if char.isalpha():
        # consider only alphabetic characters
        char = char.lower()  # convert to lowercase for uniformity
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
# Find the character with the maximum frequency
most_frequent_char = max(char_frequency, key=char_frequency.get)
print(f"The most frequent character is '{most_frequent_char}' with a frequency of {char_frequency[most_frequent_char]}.")



# Another solution using for loop

max_freq = 0
most_frequent_char = ''
for char, freq in char_frequency.items():
    if freq > max_freq:
        max_freq = freq
        most_frequent_char = char 

print(f"The most frequent character is '{most_frequent_char}' with a frequency of {max_freq}.")

