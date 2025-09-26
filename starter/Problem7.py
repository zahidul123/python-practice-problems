### Problem-7: Write a function that takes 1 number as argument. T
# he function should return “Fizz” if the number is divisible by 3, 
# the function should return “Buzz” if the number is divisible by 5, 
# the function should return “FizzBuzz” if the number is divisible by both 5 and 3, 
# otherwise return “Not a Fizz-buzz number”

def fizz_buzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

number = int(input("Enter a number: "))
print(fizz_buzz(number))