#Create a function that converts Celsius into Fahrenheit.
def temp():
        #convert celsus into fahrenheit
    cel = float(input("enter the value of celsius : "))

    # conversion logic

    fahrenheit = (cel*4.5)+32

    # print
    print(f"the given celsius is {cel} converted in fahranheit {fahrenheit}")

print(temp())