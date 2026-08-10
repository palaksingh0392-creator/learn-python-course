#Leap Year Checker
#Take a year and tell whether it is a leap year or not
year = int(input("enter the desired year :"))

#logic

if year%400 == 0 :
    print("this year is a leap year")
elif year%4 == 0 :
    print("this year is a leap year")
else :
    print("this is not a leap year")