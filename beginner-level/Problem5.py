### Problem-5: Flatten a Nested List
#You are given a nested list of elements (e.g., UI config data). Flatten it into a single-level list.
#-   **Input**: `[1, [2, 3], [4, [5]]]`
#-   **Output**: `[1, 2, 3, 4, 5]`
#-   **Hint**: Use recursion to handle sublists.

def flatten_list(nested_list):
    flated_list = []
    for item in nested_list:
        if isinstance(item,list):
            flated_list.extend(flatten_list(item))
        else:
            flated_list.append(item)
    return flated_list
print(flatten_list([1, [2, 3], [4, [5]]]))
print(flatten_list([1, [2, [3, 4]], 5, 6, [7, 8]]))
