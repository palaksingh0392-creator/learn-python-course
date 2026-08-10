# Simple Calculator

num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))

choice = input(
    "Enter the valid choice: "
    "1 - Addition, "
    "2 - Subtraction, "
    "3 - Multiplication, "
    "4 - Division: "
)

def case_one():
    total = num1 + num2
    return f"The sum of num1 and num2 is {total}"

def case_two():
    sub = num1 - num2
    return f"The subtraction of num1 and num2 is {sub}"

def case_three():
    multiplication = num1 * num2
    return f"The multiplication of num1 and num2 is {multiplication}"

def case_four():
    if num2 == 0:
        return "Division by zero is not allowed."
    
    division = num1 / num2
    return f"The division of num1 and num2 is {division}"

def default():
    return "Enter a valid choice."

def execute_case(choice):
    switcher = {
        '1': case_one,
        '2': case_two,
        '3': case_three,
        '4': case_four,
    }
    
    return switcher.get(choice, default)()

print(execute_case(choice))