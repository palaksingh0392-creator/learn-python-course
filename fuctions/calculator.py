#Create a calculator using separate functions for addition, subtraction, multiplication and division.
def add():
    total = num1 + num2
    return f"The sum of num1 and num2 is {total}"
def sub():
    sub = num1 - num2
    return f"The subtraction of num1 and num2 is {sub}"
def mul():
    multiplication = num1 * num2
    return f"The multiplication of num1 and num2 is {multiplication}"
def div():
    if num2 == 0:
        return "Division by zero is not allowed."
    
    division = num1 / num2
    return f"The division of num1 and num2 is {division}"

num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))

choice = input(
    "Enter the valid choice: "
    "1 - Addition, "
    "2 - Subtraction, "
    "3 - Multiplication, "
    "4 - Division: "
)


match choice :
    case "1":
        print(add())
    case "2":
        print(sub())
    case "3":
        print(mul())
    case "4":
        print(div())
    case _:
        print("Invalid choice.")

