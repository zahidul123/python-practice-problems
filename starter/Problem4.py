### Problem-4: Write a program to find the index of 7

numbers=[3, 5, 1, 9, 7, 2, 8 ]
print(numbers.index(7))

# another solution using loop

for i in range(len(numbers)):
    if numbers[i] == 7:
        print(i)
        break