('=======================TASK 1 =================')

v1 = int(input('Enter First Value: '))
v2 = int(input('Enter Second Value: '))
add = v1 + v2
dif = v1 - v2
mul = v1 * v2
div = v1 / v2
floor_div = v1 // v2

print('Sum of ' ,v1 ,'and', v2, 'is :', add)
print('Difference of ', v1, 'and', v2, 'is :', dif)
print('Multipliction of', v1, 'and', v2, 'is :', mul)
print('Division of ', v1, 'and', v2, 'is :', div)
print('Floor Division of ', v1, 'and', v2, 'is :', floor_div)

('== == == == == == == == TASK2 == == == == == == == == == == ==')

n1 = input("Enter Your first Value ")
n2 = input("Enter Your Second Value ")
x = n1 == n2

print("Your first value", n1, "is equal to", n2, x)

y = n1 != n2
print("Your first value", n1, "is not equal to", n2, y)

('== == == == == == == == == = TASK3 == == == == == == == == == == =')
# Area of Plot
# Area of Rectangle plot

print("Formula of Rectangle of Plot is: lenght * Width")
lenght = int(input("Enter Your Plot Lenght in Meters "))
width = int(input("Enter Your plot width in Meters "))
area = lenght * width
print('Your Area of Rectangle Plot is :', area, 'meters square')

# Area of square Plot
print("Formula of Square Plot is: lenght * length")
n1 = int(input("Enter the length of plot in meters "))
area_square = n1 * n1
print("Your Area of square Plot is :", area_square, "meters square")

# Area of Triangle plot

print("Formula of  Triangular Plot is: 0.5 * b * h, \n b is the length of the base of the triangle,\n h is the height/altitude of the triangle")
b = int(input("Enter Your Plot length of the base in Meters "))
h = int(input("Enter Your plot height/altitude in Meters "))
area_tri = 0.5 * b * h
print('Your Area of Rectangle Plot is :', area_tri, 'meters square')


('== == == == == == == == == == =TASK 4 == == == == == == == == == == == == ==')

# BMI Calculator
# Metric Unit

age = int(input('Enter Your Age: '))
gender = input('Enter Your Gender: ')
height = float(input('Enter Your Height in CM: '))
weight = float(input('Enter Your weight in KG: '))
bmi = weight / (height / 100) ** 2

print("Your BMI is:", bmi)

# BMI Calculator
# US Unit

age = int(input('Enter Your Age: '))
gender = input('Enter Your Gender: ')
h = float(input('Height in Feet and Inches: '))
w = float(input('Enter Your weight in Pounds: '))
bmi = 703 * (w / h ** 2)

print("Your BMI is:", bmi, "kg/m2")


('== == == == == == == == == == = Task 5 == == == == == == == == ==')

# Convert Weight KG into Pounds

w = float(input("Enter Your Weight in Kgs "))
weight = w * 2.2                                #Formula for conversion of kg into pounds
print("Your weight is : ", weight, 'pounds')

# Convert Height into inches

h = float(input("Enter Your height in feet "))
height = h * 12                                     #formula for Conversion of feet into inchec
print("Your height is : ", height, 'Inches')

# convert Redian into Degree
pi = 22 / 7                                                   # Value of pi
radian = float(input("Enter radians value: "))
degree = radian * (180 / pi)                            # formula for conversion of redian into degree
print("The value of Degree is: ", degree)



('== == == == == == == == == == == = task 6 == == == == == == == == == == == == == =')


# Area of Trapezoid
print("Formula of Area of Trapezoid = (a+b/2)*h")

"a = Base of plot"
"b = base of plot"
"h = height"

a = int(input("Enter value of base "))
b = int(input("Enter value of base "))
h = int(input("Enter value of height "))

area_trapezoid = ((a + b) / 2) * h                  #formula for area of trapezoid plot/land
print("Area of trapezoid is :", area_trapezoid)

# Area of Parallelogram

print("Formula of Area of parallelogram = b*h")

"b = base of plot"
"h = height"
b = float(input("Enter value of base "))
h1 = float(input("Enter value of height "))

area_pall = b * h1                                   #formula for area of parallelogram plot/land
print("Area of Parallelogram is :", area_pall)

# Area of Cylinder

print("Formula of Area of cylinder = A=2prh+2pr**2")
"pi = 22/7"
"r = ridus of cylinder"
"h = height of cylinder"
r = float(input("Enter value of ridus of Cylinder: "))
h2 = float(input("Enter value of height of cylinder: "))
pi = 22 / 7

area_cylinder = A = (2 * pi * r * h2) + (2 * pi * r ** 2 )           #formula for area of Cylinder
print("Area of Cylinder :", area_cylinder)
