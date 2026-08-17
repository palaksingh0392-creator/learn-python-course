#Create a function that takes a number and returns its factorial using a loop.

def fact():
        #Factorial
    #Take a number N and calculate N! using a loop. Example: 5! = 120.
    num = int(input("enter the desired value:"))
    fact = 1
    for i in range (1, num+1 ):
        fact = fact * i
        print(f"the factorial of no.{i} is {fact} ")

print(fact())