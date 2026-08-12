#Fibonacci Series
#Take the number of terms and print the Fibonacci series. Example: 0 1 1 2 3 5 8

num = int(input("enter the desired value:"))
f=0
s=1
for i in range (1, num+1 ):
    print(f, end=" ")
    t=f+s
    f=s
    s=t
