### Problem-10: The list below is the collection of the ages of people from a village.
# Clean up the data and store only numbers in another list.

data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
cleaned_data = []
for item in data_list:
    if isinstance(item, (int,float,complex)): # check if item is a number
        cleaned_data.append(item)

print(cleaned_data)