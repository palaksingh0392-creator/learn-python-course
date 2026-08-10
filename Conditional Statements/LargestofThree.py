#Larger of Two
num1 = int(input("enter the value of num1 :"))
num2 = int(input("enter the value of num2 :"))
num3 = int(input("enter the value of num3 :"))
#applied logic 
if num1 > num2 > num3 :
    print("the num1 is greator than num2 and num2 is greator than num3")
elif num3 > num2 > num1:
    print("the num3 is greator than num2 and num2 is greator than num1")
elif num2 > num1 > num3:
    print("the num2 is greator than num1 and num1 is greator than num3")
elif num1 > num2 < num3:
    print("the num1 is greator than num2 and num2 is less than num3")
elif num2 > num3 < num1:
    print("the num2 is greator than num3 and num3 is less than num3")
elif num3 > num1 < num2:
    print("the num3 is greator than num1 and num1 is less than num3")
else :
    print("the num1 and num2 or num3 is equal")