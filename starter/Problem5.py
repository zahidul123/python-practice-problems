### Problem-5: Write a program to sort the numbers in Ascending order

numbers=[3, 5, 1, 9, 7, 2, 8 ]
numbers.sort()
print(numbers)

# another solution using loop
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]: #logic to swap
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)