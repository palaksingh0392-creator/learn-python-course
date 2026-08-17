# 7. Ask the user for a name and check whether it exists in a student-name list
size = int(input("enter the value of size:"))
names = []
for i in range(size):
    value = input(f"enter the name:")
    names.append(value)
name = input("enter your name to check:")
print(name in names)
