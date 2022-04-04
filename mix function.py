# Program to check if a number is prime or not
print("============= PRIME Numbers ===================")


def prime():  # To check whether the number is even or not
    num = int(input("Enter No "))
    if num >= 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                #                                                            print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


prime()

print("============== ODD Numbers ===================")


def odd():  # To check whether the number is Odd or not
    number = int(input('Enter Numbers =====> '))
    if (number % 2) != 0:
        print(number, 'is ODD Numbers')
    else:
        print(number, "is not ODD Numbers")


odd()

print(" ============= EVEN Numbers ===================")


def even():
    number = int(input('Enter Numbers =====> '))
    if (number % 2) == 0:
        print(number, 'is EVEN Numbers')
    else:
        print(number, "is not EVEN Numbers")


even()

print(" ================ MIX Numbers =====================")


def mix():
    x = int(input("Enter NO "))
    if x >= 1:
        print(x, "No is Positive integer")
    if x < 0:
        print(x, "No is Negative integer")
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                pass
        else:
            print(x, "is a prime number")

    if (x % 2) == 0:
        print(x, 'is EVEN Numbers')
    if (x % 2) != 0:
        print(x, 'is ODD Numbers')


mix()
