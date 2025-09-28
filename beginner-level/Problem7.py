### Problem-7: Find Missing Number in a Sequence
# You received log files indexed from 1 to n. One log is missing. Find it.
# -   **Input**: `[1, 2, 4, 5]`
# -   **Output**: `3`
# -   **Hint**: Use arithmetic formula for sum of n numbers.

def find_missing_number(num_list):
    n = len(num_list) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(num_list)
    return expected_sum - actual_sum
print(find_missing_number([1, 2, 4, 5]))