current_bal = 5000
while True:
    print("Enter Your Choice, 1. Deposit ,2. Withdraw, 3. Check Balance, 4. Exit ")
    ch = int(input(""))
    if ch == 1:
        p1 = int(input("Enter deposit amount "))
        current_bal += p1
        print("Your current balance", current_bal)
    elif ch == 2:
        w1 = int(input("Enter Withdraw Amount "))
        if w1 <= current_bal:
            print("You have withdraw your amount ", w1)
            current_bal = current_bal-w1
        else:
            print("You don't have enough balance")
    elif ch == 3:
        print("Your Current balance is ", current_bal)
    elif ch == 4:
        print("Thanks, BYE")
        break
    else:
        print("You have selected wrong choice")



