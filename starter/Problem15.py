### Problem-15: Write conditional statements to identify the student’s average marks. 
# If any subject’s mark is less than 40, you should print FAILED instead of making average marks

lstudent_1 = [40, 35, 70, 90, 56]

student_2 = [57, 35, 80, 98, 46]

# all() function returns True if all items in an iterable are true, otherwise it returns False.

def check_result_v2(marks):
    if all(mark >= 40 for mark in marks):
        average = sum(marks) / len(marks)
        return f"PASSED with average marks: {average}"
    else:
        return "FAILED"
    
print(check_result_v2(lstudent_1))
print(check_result_v2(student_2))