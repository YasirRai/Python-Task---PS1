# create function of ATM


def atm(deposit, withdraw, balance, qut):
    current_bal = 5000
    print("Enter Your Choice, 1. Deposit ,2. Withdraw, 3. Check Balance, 4. Exit ")
    ch = int(input("Enter Choice "))
    if ch == 1:
        p1 = int(input("Enter deposit amount "))
        current_bal += p1
        print("Your current balance", current_bal)

    if ch == 2:
        w1 = int(input("Enter Withdraw Amount "))
        if w1 <= current_bal:
            print("You have withdraw your amount ", w1)
            current_bal = current_bal - w1
        else:
            print("You don't have enough balance")
    if ch == 3:
        print("Your Current balance is ", current_bal)
    if ch == 4:
        print("Thanks, BYE")


atm(1, 2, 3, 4)

'============================= 2nd Method========================================='


def atm():
    while True:
        current_balance = 5000
        print('Enter Your Choice, 1. Deposit ,2. Withdraw, 3. Check Balance, 4. Exit ')
        ch = int(input("Enter Choice "))
        if ch == 1:
            deposit()
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break
        if ch == 2:
            withdraw()
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break

        elif ch == 3:
            print("Yours Current balance is ", current_balance)
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break
        elif ch == 4:
            print("Thanks , BYE")
            exit()
            break


atm()


def deposit():
    bal = 5000
    cho = int(input("Enter Deposit Amount "))
    bal = cho + bal
    print("Your Current Balance ", bal)


def withdraw():
    current_bal = 5000
    w1 = int(input("Enter Withdraw Amount "))
    if w1 <= current_bal:
        print("You have withdraw your amount ", w1)
        current_bal = current_bal - w1
    else:
        print("You don't have enough balance")
