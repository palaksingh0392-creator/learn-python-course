# Remove duplicate values from a list. Try solving it first using loops rather than searching for a one-line
# solution.
size = int(input("enter the value of size :"))
num = []
for i in range(size):
    value = int(input(f"enter the value of num{i} :"))
    num.append(value)
unique= []
for i in range(size):
   if num[i] not in unique:
    unique.append(num[i])
print("list removing duplicates:", unique)


