### Problem-14: Sort the list in DESCENDING order and find the subtraction of maximum and minimum numbers.

list_1 = [4, 9, 8, 7, 5, 2, 13]

for i in range(len(list_1)):

    for j in range(i+1, len(list_1)):
        # I use selection sort logic here
        if list_1[i] < list_1[j]: #logic to swap for descending order
            #in java or kotlin we use a temp variable to swap
            # temp = list_1[i]
            # list_1[i] = list_1[j]
            # list_1[j] = temp
            # but in python we can do it in one line
            list_1[i], list_1[j] = list_1[j], list_1[i]


print("Sorted list in descending order (using loop):", list_1)
subtraction_loop = list_1[0] - list_1[-1] # max - min
print("Subtraction of max and min (using loop):", subtraction_loop)