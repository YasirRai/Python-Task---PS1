import math
s = math.sqrt(64)
s1 = math.ceil(77.08)
print(s, s1)


# Function for BMI Calculator ( Metric Unit )

age = int(input('Enter Your Age: '))
gender = input('Enter Your Gender: ')
height = float(input('Enter Your Height in CM: '))
weight = float(input('Enter Your weight in KG: '))
bmi = weight / (height / 100) ** 2

print("Your BMI is:", bmi.__round__(2))

# BMI Calculator
# US Unit

a = int(input('Enter Your Age: '))
g = input('Enter Your Gender: ')
h = float(input('Height in Feet and Inches: '))
w = float(input('Enter Your weight in Pounds: '))
bmi = 703 * (w / h ** 2)

print("Your BMI is:", bmi, "kg/m2")
