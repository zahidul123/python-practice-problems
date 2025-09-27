### Problem-1: Reverse a String Without Slicing
# You are building a simple text utility tool for your web app. 
# One of the requirements is to reverse a string input by a user.
# **Input**: `"bongodev"`
# **Output**: `"vedognob"`
# **Hint**: Use a loop to read the string from end to start.

input_string = "bongodev"
reversed_string = ""
for letter in input_string:
    #current content add first and previous one after
    reversed_string = letter + reversed_string

print(reversed_string)