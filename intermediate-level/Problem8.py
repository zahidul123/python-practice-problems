### Problem-8: Command-line Calculator
#Build a CLI tool that takes command `add 5 7` and returns `12`.
#-   **Hint**: Parse `input().split()` and use if/elif for commands.

user_input = input("Enter command (e.g., 'add 5 7'): ")
split_command = user_input.split()
    
if len(split_command) != 3:
    print("Invalid input format. Use: <operation> <num1> <num2>")
    exit(1)
    
operation, num1, num2 = split_command
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Please enter valid numbers.")
    exit
    
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 == 0:
        print("Error: Division by zero.")
        exit(1)
    result = num1 / num2
else:
    print("Unsupported operation. Use add, subtract, multiply, or divide.")
        
    
print(f"Result: {result}")