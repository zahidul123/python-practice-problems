### Problem-1: Longest Word in a Sentence
#Build a function that extracts the longest word from user-generated content.
#  **Input**: `"Machine learning is fascinating"`
#  **Output**: `"fascinating"`
#  **Hint**: Split string and use `max()` with `key=len`.

def longest_word(sentence):
    words = sentence.split()
    print(words)
    longest = max(words, key=len)

    return longest

#print(longest_word("Machine learning is fascinating"))

sentense = input("Enter a sentence: ")
print("The longest word is:", longest_word(sentense))

