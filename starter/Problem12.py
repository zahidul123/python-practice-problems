### Problem-12: Find the common items between the lists and make SUM of the new list items which are common between the lists.

list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]
set1=set(list1)
set2=set(list2)
print("set1:", set1)
print("set2:", set2)

common_items = list( set1 & set2 ) # intersection of two sets for example it takes only similar items
print("Common items:", common_items)
print("Sum of common items:", sum(common_items))



# another solution using list comprehension

common_items_lc = list(set([item for item in list1 if item in list2]))
print("Common items (using list comprehension):", common_items_lc)
print("Sum of common items (using list comprehension):", sum(common_items_lc))