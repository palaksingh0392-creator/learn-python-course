#Create a function that takes a number and tells whether it is even or odd.

def find():
        #Even or Odd
    num = int (input("enter the value of num:"))

    #logic 
    if num%2 == 0 :
        print("the entered value is even",num )
    else :
        print("the entered value is odd",num )

print(find())