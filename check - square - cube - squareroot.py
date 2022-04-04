'============================ Square ROOT ===================='


def square():
    s = int(input("Enter square value "))
    s1 = (s ** (1 / 2))
    if s > 0:
        if s1 % 1 == 0:
            print(f"This is Perfect Square value of'{s}' is ", s1)
        else:
            print("sorry ! This is not perfect square ")
    else:
        print("Enter Positive Value only")

'=========================== Cube ======================'


def cube():
    c = int(input("Enter value to Check Cube "))
    c1 = c ** (1 / 3)
    if c1 % 1 == 0:
        print("This is Perfect cube & value is ", c)
    else:
        print("Sorry ! This is not Perfect cube")


