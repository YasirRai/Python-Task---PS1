# Design a control applications for your home appliances
appliance = ["tv", "fans", "bulb lights"]
print("Home Appliance are tv, fan, bulb")
while True:
    choice = input("Please Select appliances ")
    if choice == 'tv':
        while True:
            tv_on = input("Press 'Y' to  Switch ON , Press 'N' to Switch OFF the TV  , Press 'E' for EXIT")
            if tv_on == 'y':
                print(choice, " is Switch On Now ")
            elif tv_on == 'n':
                print(choice, " is Switch OFF Now ")
            elif tv_on == 'e':
                break
    if choice == 'fan':
        while True:
            tv_on = input("Press 'Y' to  Switch ON , Press 'N' to Switch OFF the TV  , Press 'E' for EXIT")
            if tv_on == 'y':
                print(choice, " is Switch OFF Now")
            elif tv_on == 'n':
                print(choice, " is Switch OFF Now")
            elif tv_on == 'e':
                break
    if choice == 'bulb':
        while True:
            tv_on = input("Press 'Y' to  Switch ON , Press 'N' to Switch OFF the TV  , Press 'E' for EXIT")
            if tv_on == 'y':
                print(choice, " is Switch OFF Now")
            elif tv_on == 'n':
                print(choice, " is Switch OFF Now")
            elif tv_on == 'e':
                break
    else:
        print("Select Appliance", appliance, "or Press 'E' for EXIT")
        ch = input("")
        if ch == 'e':
            pass
    break




