#Take number of days and convert it into hours, minutes and seconds.
day = int(input("enter the no of days:"))

#conversion

hours = day * 24
minutes= hours *60
seconds = minutes*60

print(f"the day {day} has {hours} hours, {minutes} minutes, {seconds} seconds")
