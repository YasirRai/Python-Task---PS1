# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
#    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + dis) / (2 * a))
        print((-b - dis) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", dis)
        print(- b / (2 * a), " - i", dis)

    # Driver Program


a = int(input("Enter Value of A "))
b = int(input("Enter Value of B "))
c = int(input("Enter Value of C "))

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
