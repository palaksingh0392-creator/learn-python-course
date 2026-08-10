#Simple Interest
#Take principal, rate and time. Calculate SI = (P x R x T) / 100.

p = float(input("enter the principal amount:"))
r = float(input("enter the rate of interest:"))
t = float(input("enter the time limit:"))

SI = (p * r * t) / 100

print(f"the value of SI is {SI}")