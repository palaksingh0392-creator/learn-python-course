#Ask the user to choose Circle, Rectangle or Square. Ask whether they want Area or Perimeter.
#Accept dimensions only between 1 and 100. Calculate accordingly

choice = int(input("enter the choice, 1 - circle , 2 - rectangle , 3 - square :"))
mode = int(input("enter 1 - area or 2 - perimeter :"))
#circle
if choice == 1 :
    print ("the enter choice is circle")
    r = int(input("enter the radius r :"))
    #check
    if r > 100:
        print("enter the value less than 100")    
        r = int(input("enter the radius r :"))
    #condition
    if mode == 1 :
        area = 3.15*r*r
        print(f"the area of circle is {area}")
    elif mode == 2:
        perimeter = 2*3.15*r
        print(f"the perimeter of circle is {perimeter}")
#rectangle
elif choice == 2 :
    print ("the enter choice is rectangle")
    l = int(input("enter the length :"))
    #check
    if l > 100:
        print("enter the value less than 100")
        l = int(input("enter the length :"))
    b = int(input("enter the breadth :"))
    if b > 100:
        print("enter the value less than 100")
        b = int(input("enter the breadth :"))
    #condition
    if mode == 1 :
        area = l*b
        print(f"the area of rectangle is {area}")
    elif mode == 2:
        perimeter = 2*(l+b)
        print(f"the perimeter of rectangle is {perimeter}")
#square
elif choice == 3 :
    print ("the enter choice is square")
    a = int(input("enter the side :"))
    #check
    if a > 100:
        print("enter the value less than 100")
        a = int(input("enter the side :"))
    #condition
    if mode == 1 :
        area = a*a
        print(f"the area of square is {area}")
    elif mode == 2:
        perimeter = 4*a
        print(f"the perimeter of square is {perimeter}")
    