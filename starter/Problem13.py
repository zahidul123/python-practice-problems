### Problem-13: Compare the two dictionaries and find the common items based on KEYs of the dictionaries

dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}

dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

common_keys = set(dict1.keys()) & set(dict2.keys())
print("Common keys:", common_keys)


# another solution using list comprehension

common_keys_lc = [key for key in dict1 if key in dict2]
print("Common keys (using list comprehension):", common_keys_lc)