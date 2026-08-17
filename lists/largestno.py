# 4. Find the largest number in a list using a loop.
size = int(input("enter the value of size :"))
num = []
for i in range(size):
    value = int(input(f"enter the value of num{i} :"))
    num.append(value)

largest = num[0]
for i in range(size):
    print(num[i])
    if num[i] > largest:
        largest  = num[i]
   
print(f"largest is {largest}")