#Take an amount and discount percentage. Calculate final price after discount
amount = float(input("enter the value of amount:"))
discount = float(input("enter the value of discount:"))
# discount percentage.
cal = amount - (amount* discount/100)
print(f"the amount applied before discount is {amount}")
print(f"the amount applied after discount is {cal}")