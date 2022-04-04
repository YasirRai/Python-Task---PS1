# create Factorial Function
def fact():
    no = int(input("Enter Values "))
    factorial = 1
    if no < 0:
        print("Factorial does not exist for negative numbers")
    elif no == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, no + 1):
            factorial = factorial * i
        print("Factorial of", no, "is", factorial)


fact()
