# Design Vending Machine
print("Wellcome to Vending Machine")

ice_cream = ['mango', 'pista', 'orange', 'rainbow', 'vanilla']
chocolates = ['dairy milk', 'perk', 'kitkat', 'twix', 'mars']
chips = ('lays', 'kurkure', 'asli baba', 'kurleez', 'wavy')
coldrink = ('pepsi', 'marinda', '7up', 'deo', 'sprite')
juice = ('slice', 'apple', 'red grapes', 'chounsa', 'orange')

while True:
    print(" '1' for ice cream", " '2' for chocolates", "'3' for chips", "'4' for colddrink", " '5' for juices")
    choice = int(input("Please Select Code for Buy "))
    if choice == 1:
        print("You Selected Ice-Cream and Choose flavour to Buy", ice_cream)
        ice = input("Enter Your item to buy ")
        ice_stock = 200
        qty = int(input("How much Quantity Do you Want? "))
        if qty > 0 or qty <= 40:
            print("You  got", str(qty), "" + ice, "Ice Cream")
            ext = input("Do you want to Buy Press Y or Press N  for EXIT ")
            if ext == 'y':
                pass
            elif ext != 'y':
                break
            elif qty > 40:
                print("SORRY! Minimum Quantity is 40")
                ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
                if ext == 'y':
                    pass
                else:
                    break
    elif choice == 2:
        print("You Selected Chocolates and Choose flavour to Buy", chocolates)
        ice = input("Enter Your item to buy ")
        qty = int(input("How much Quantity Do you Want? "))
        if qty > 0 or qty <= 40:
            print("You  got", str(qty), "" + ice, "Chocolates")
            ext = input("Do you want to Buy Press Y or Press N  for EXIT ")
            if ext == 'y':
                pass
            elif ext != 'y':
                break
            elif qty > 40:
                print("SORRY! Minimum Quantity is 40")
                ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
                if ext == 'y':
                    pass
                else:
                    break
    elif choice == 3:
        print("You Selected Ice-Cream and Choose flavour to Buy", chips)
        ice = input("Enter Your item to buy ")
        qty = int(input("How much Quantity Do you Want? "))
        if qty > 0 or qty <= 40:
            print("You  got", str(qty), "" + ice, "Chips")
            ext = input("Do you want to Buy Press Y or Press N  for EXIT ")
            if ext == 'y':
                pass
            elif ext != 'y':
                break
            elif qty > 40:
                print("SORRY! Minimum Quantity is 40")
                ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
                if ext == 'y':
                    pass
                else:
                    break
    elif choice == 4:
        print("You Selected Ice-Cream and Choose flavour to Buy", coldrink)
        ice = input("Enter Your item to buy ")
        qty = int(input("How much Quantity Do you Want? "))
        if qty > 0 or qty <= 40:
            print("You  got", str(qty), "" + ice, "Cold Drinks")
            ext = input("Do you want to Buy Press Y or Press N  for EXIT ")
            if ext == 'y':
                pass
            elif ext != 'y':
                break
            elif qty > 40:
                print("SORRY! Minimum Quantity is 40")
                ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
                if ext == 'y':
                    pass
                else:
                    break
    elif choice == 5:
        print("You Selected Juices and Choose flavour to Buy", juice)
        ice = input("Enter Your item to buy ")
        qty = int(input("How much Quantity Do you Want? "))
        if qty > 0 or qty <= 40:
            print("You  got", str(qty), "" + ice, "Juices")

            ext = input("Do you want to Buy Press Y or Press N  for EXIT ")
            if ext == 'y':
                pass
            elif ext != 'y':
                break
            elif qty > 40:
                print("SORRY! Minimum Quantity is 40")
                ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
                if ext == 'y':
                    pass
                else:
                    break
    else:
        print("Please Choose Product")
        ext = input("Do You Want to Buy Again  Press Y or Press any key for Exit ")
        if ext == 'y':
            pass
        else:
            break
