class BankAccount:

    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        print('Wellcome to Skillevetion Banking System'.center(80))

    def deposit(self):
        dep = int(input('Enter Your amount to add: '))
        self.balance += dep
        print('You have deposit', dep, 'amount \n your current balance is ', self.balance)


    def withdraw(self):
        witdrw = int(input("Enter amount to withdraw: "))
        self.balance -= (witdrw+self.fee)
        print('You have withdraw', witdrw, 'amount \n your current balance is ', self.balance)


    def bankfees(self):
        self.fee = self.balance * 0.05
        print('Fee for every withdraw transaction is', self.fee, ' \n Your current balance is ', self.balance)

    def display(self):
        print("Account holder Name: ", acc.name, "\nAccount No: ", acc.accountNumber, "\nCurrent Balance:", acc.balance)


acc = BankAccount(1234, 'yasir', 5000)
while True:
    ch = int(input(' 1: Deposit \n 2: Withdraw \n 3: Account details \n 4: Bank fees \n Select option :'))

    if ch == 1:
        acc.deposit()
        ex = input("Do you want Another Transaction ? Press 'y' or Any key for Exit")
        if ex == 'y':
            continue
        else:
            exit()
    elif ch == 2:
        acc.withdraw()
        ex = input("Do you want Another Transaction ? Press 'y' or Any key for Exit")
        if ex == 'y':
            continue
        else:
            exit()
    elif ch == 3:
        acc.display()
        ex = input("Do you want Another Transaction ? Press 'y' or Any key for Exit ")
        if ex == 'y':
            continue
        else:
            exit()
    elif ch == 4:
        acc.bankfees()
        ex = input("Do you want Another Transaction ? Press 'y' or Any key for Exit ")
        if ex == 'y':
            continue
        else:
            exit()
    else:
        print("Wrong Selection")
