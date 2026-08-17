#Create a function that takes marks of 3 subjects and returns the average.

def avg():
    num1 = int (input("enter the value of num1 :"))
    num2 = int (input("enter the value of num2 :"))
    num3 = int (input("enter the value of num3 :"))

    sum = num1+num2+num3
    average = sum/3
    print(f"the average of {num1}, {num2}, {num3} is {average}")
print(avg())