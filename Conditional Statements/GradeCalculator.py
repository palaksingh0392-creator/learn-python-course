#Grade Calculator 
# Take marks from 0-100. Show A for 90-100, B for 80-89, C for 70-79, D for 60-69, otherwise Fail.Reject values below 0 or above 100.
sub1 = float(input("enter marks of hindi out of 20:"))
if sub1 >20 :
    print("enter the value less than 20")
    sub1 = float(input("enter marks of hindi out of 20:"))
sub2 = float(input("enter marks of engish out of 20:"))
if sub2 >20 :
    print("enter the value less than 20")
    sub2 = float(input("enter marks of english out of 20:"))
sub3 = float(input("enter marks of maths out of 20:"))
if sub3 >20 :
    print("enter the value less than 20")
    sub3 = float(input("enter marks of maths out of 20:"))
sub4 = float(input("enter marks of sst out of 20:")) 
if sub4 >20 :
    print("enter the value less than 20")
    sub4 = float(input("enter marks of sst out of 20:")) 
sub5 = float(input("enter marks of science out of 20:"))
if sub5 >20 :
    print("enter the value less than 20")
    sub5 = float(input("enter marks of science out of 20:"))

total = sub1+sub2+sub3+sub4+sub5
print(f"the marks of subjects are:")
print(f"sub1 : {sub1}, sub2 : {sub2}, sub3 : {sub3}, sub4 : {sub4}, sub5 : {sub5} ")
print(f"the total is:{total}")
if total >= 90 < 100:
    print(f"the grade is A on total {total}")
elif total > 80 < 89:
    print(f"the grade is B on total {total}")
elif total > 70 < 79:
    print(f"the grade is c on total {total}")  
elif total > 60 < 69:
    print(f"the grade is d on total {total}")  
else :
    print(f"the student failed on total {total}")
    