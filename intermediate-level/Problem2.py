### Problem-2: Group Anagrams Together
#Group similar words together in a UI (e.g., tags: `["bat", "tab", "cat", "act"]`).

#-   **Output**: `[["bat", "tab"], ["cat", "act"]]`
    
#-   **Hint**: Use a dictionary where sorted word is key.

def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word)) # Sort the word to form the key 
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return list(anagrams.values())

print(group_anagrams(["bat", "tab", "cat", "act", "dog", "god", "evil", "vile","atb"]))