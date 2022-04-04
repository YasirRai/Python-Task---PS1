currency = [{"pkr": 179.20 , "dollar": 1, "euro": 0.86, "inr": 90, "yen": 117}]
   # display currency list
while True:
    u = input("Which currency do you want to convert?  ")   # get value from users
    if u in currency:
        u2 = input("currency converted into ")
        if u == 'pkr' or "Pkr":
            curr = int(input('Enter amount '))
            convert_pkr = curr/120
#            convert_usd = curr*179.20
            print("Pakistani Rupees in", u2, "is", round(convert_pkr, 2))
#            print("US Dollar in PKR", convert_usd)
            ext = input("Do You want to convert currency Press 'Y' or Quit? ")
            if ext != 'y' and ext != 'Y':
                break
            else:
                continue

    if u != currency:
        print("Please select from list", currency)
        ext = input("Do You want to convert currency Press 'Y' or Quit? ")
        if ext != 'y' and ext != 'Y':
            break


