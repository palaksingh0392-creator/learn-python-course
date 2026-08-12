# Count Digits
# Take a whole number and count how many digits it contains.

num = int(input("Enter a whole number: "))

original_num = num
count = 0
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    count += 1

print(f"Count of {original_num} is {count}")
