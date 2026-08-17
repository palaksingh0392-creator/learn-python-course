# Take 5 marks, store them in a list and display total, average, highest and lowest marks.
size = 5
num = []
for i in range(size):
    value = float(input(f"enter the marks upto 20:"))
    if value <=20:
        num.append(value)
    else :
        print("enter value less than 20")
        value = float(input(f"enter the marks upto 20:"))   
choice = int(input("choose operation : 1 for display total , 2 for average, 3 - highest marks, 4 - lowwest marks: "))
while(True):
    match choice:
        case 1 :
            sum = 0
            for i in range(size):
                sum = sum + num[0]
            print(f"the total is {sum}")
            break
        case 2 :
            sum = 0
            for i in range(size):
                sum = sum + num[0]
            print(f"the total is {sum}")
            avg = sum/5
            print(f"the average of total is {avg}")
            break
        case 3 :
            largest = num[0]
            for i in range(size):
                print(num[i-1])
                if num[i-1] > largest:
                    largest  = num[i]
            
            print(f"largest is {largest}")
            break
        case 4 :
            smallest = num[0]
            for i in range(size):
                print(num[i-1])
                if num[i-1] <= smallest:
                    smallest  = num[i]
            
            print(f"smallest is {smallest}")
            break