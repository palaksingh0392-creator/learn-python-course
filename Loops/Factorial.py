#Factorial
#Take a number N and calculate N! using a loop. Example: 5! = 120.
num = int(input("enter the desired value:"))
fact = 1
for i in range (1, num+1 ):
    fact = fact * i
    print(f"the factorial of n no.{i} is {fact} ")