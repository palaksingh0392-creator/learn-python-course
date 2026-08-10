#Take units used. Use rates: 0-100 units = Rs 5/unit, 101-200 = Rs 7/unit, above 200 = Rs 10/unit.
#Calculate the bill according to your chosen rule.

unit = float(input("enter the units:"))
bill = 0
#logic 
if unit > 0 < 100 :
    bill = unit * 5 
    print(f"your applied bill on unit {unit} is {bill}")
elif unit > 101 <200 :
    bill = unit * 7
    print(f"your applied bill on unit {unit} is {bill}")
elif unit > 200 :
    bill = unit * 10 
    print(f"your applied bill on unit {unit} is {bill}")
