#Sum 1 to N
#Take N and calculate 1 + 2 + ... + N.
num = int(input("enter the desired value:"))
sum=0
for i in range (1,num+1):
    print(i)
    sum= sum+i 
print(f"the sum of n elements {num} is {sum}" )