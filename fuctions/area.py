#Create a function that takes length and breadth and returns the area of a rectangle.

def area():
        # calculate area of rectangle 
    length = int(input("enter the value of length:"))
    breadth = int(input("enter the value of breadth:"))

    # rectangle of area logic
    area = length * breadth

    #print 
    print(f"the area of length {length} and breadth {breadth} is {area} ")

print(area())
