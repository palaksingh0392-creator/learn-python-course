# Student Percentage - Calculate total and percentage.
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

#calculation logic
cal = sub1+sub2+sub3+sub4+sub5
per = cal/100 *100
print(f"the marks of subjects are:")
print(f"sub1 : {sub1}, sub2 : {sub2}, sub3 : {sub3}, sub4 : {sub4}, sub5 : {sub5} ")
print(f"the sum is:{cal} and percentage is :{per}")
