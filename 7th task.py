# Design an ATM machine
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
ch = int(input("Enter Your Choice "))
current_bal = 5000

if ch == 1:
    p1 = int(input("Enter deposit amount "))
    current_bal += p1
    print("Your current balance", current_bal)
elif ch == 2:
    w1 = int(input("Enter Withdraw Amount "))
    if w1 <= current_bal:
        print("You have withdraw your amount ", w1)
    else:
        print("You don't have enough balance")
elif ch == 3:
    print("Your Current balance is ", current_bal)
else:
    print("You have selected wrong choice")

# selecting your position  either as a programmer or management person in Game Xone
game_xone = int(input("Enter Your Experience "))
exp = (4, 5)
if game_xone in exp:
    print("You hired as a Developer ")
else:
    print("you are shortlisted for Management")

# Design a career counseling system for students to select their field
h1 = ("arts", "drawing", "management")
h2 = ("programming", "problem solving", "technologies")
h3 = ("bio", "science", "discipline and development of humanity")
hobby = input("Enter Your Hobbies and Interest ")
if hobby in h1:
    print("Your best career in field of Arts ")
elif hobby in h2:
    print("Your career in Engineering domain ")
elif hobby in h3:
    print("You should go in Medical field")
else:
    print("You have not entered anything")