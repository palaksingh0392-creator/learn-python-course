# Prime Number Checker
#Take a number and use a loop to check whether it has any divisor other than 1 and itself.

num = int(input("enter the value :"))
count = 0
#logic
for i in range (1, num+1) :
    if num % i == 0 :
        count+=1
        print(i)
if count == 2:
    print("The no. is prime")
else :
    print("it is not prime")