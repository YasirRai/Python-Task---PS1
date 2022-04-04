# function that calculates the radius and diameter of circle
def circle():
    c = int(input("Circumference of Circle (CM)? "))    # Circumference Value
    pi = 3.14
    r = c/(2 * pi)      # Radius formula
    circum = 2 * pi * r    # Circumference formula
    d = 2*r             # formula for Diameter
    print("Radius of Circle ", r.__round__(3), " CM")
    print("Diameter of Circle ", d.__round__(3), " CM")


circle()

