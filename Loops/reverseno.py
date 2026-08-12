#Reverse a Number
#Take a number such as 12345 and print 54321.

num = int(input("enter the value :"))

original_num = num
count = 0
rev = 0

while num > 0 :
    digit = num % 10
    rev = rev *10 + digit
    num = num // 10
    count +=1
print("Reverse number =", rev)
