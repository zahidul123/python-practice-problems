### Problem-3: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder
def elder_brother(age1, age2):
    if age1 > age2:
        return "Brother 1 is elder"
    elif age2 > age1:
        return "Brother 2 is elder"
    else:
        return "Both brothers are of the same age"
    
print(elder_brother(25, 30))