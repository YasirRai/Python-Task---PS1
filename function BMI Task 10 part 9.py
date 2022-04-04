# Create a function to measure BMI
def bmi():
    age = int(input('Enter Your Age: '))
    gender = input('Enter Your Gender: ')
    height = float(input('Enter Your Height in CM: '))
    weight = float(input('Enter Your weight in KG: '))
    b = weight / (height / 100) ** 2

    print("Your BMI is:", b.__round__(2))


bmi()


# BMI Calculator , US Unit

def usbmi():
    a = int(input('Enter Your Age: '))
    g = input('Enter Your Gender: ')
    h = float(input('Height in Feet and Inches: '))
    w = float(input('Enter Your weight in Pounds: '))
    usunit = 703 * (w / h ** 2)

    print("Your BMI is:", usunit, "kg/m2")


usbmi()
