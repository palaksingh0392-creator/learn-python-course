# 6. Count how many even and odd numbers are present in a list
size = int(input("enter the value of size:"))
num = []
count = 0
mount = 0
for i in range(1, size+1):
    num.append(i)
    print(num[i-1])
    if num[i-1]%2==0 :
        count+=1
    else :
        mount+=1
print(f"the count of even no present {count} and odd no present {mount} ")