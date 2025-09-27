### Problem-3: Find Duplicates in a List
#You’re given a user-uploaded list of tags. Identify duplicates for suggestion cleanup.
#-   **Input**: `["ai", "ml", "python", "ml", "dl", "ai"]`
#-   **Output**: `["ml", "ai"]`
#-   **Hint**: Use a dictionary or set to track seen elements.

input_list = ["ai", "ml", "python", "ml", "dl", "ai"]
seen = set()
duplicates = set()
for tag in input_list:
    if tag in seen:
        duplicates.add(tag)
    else:
        seen.add(tag)
print(list(duplicates))

# another way
duplicate_dict = {}
for tag in input_list:
    if tag in duplicate_dict:
        duplicate_dict[tag] += 1
    else:
        duplicate_dict[tag] = 1
duplicates = [tag for tag, count in duplicate_dict.items() if count > 1]
print(duplicates)