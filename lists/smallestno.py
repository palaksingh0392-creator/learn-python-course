# 5. Find the smallest number in a list using a loop.
size = int(input("enter the value of size:"))
num = []
for i in range(size):
    value = int(input(f"enter the value of num{i}:"))
    num.append(value)
smallest = num[0]
for i in range(size):
    print(num[i])
    if num[i] < smallest:
        smallest = num[i]
print(smallest)