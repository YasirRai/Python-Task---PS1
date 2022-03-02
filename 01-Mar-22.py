'''
You are instructed to design a vending machine that ask user to choose from
Coldrink and Chochlates
If user select coldrink then ask them which coldrink
Pepsi, fanta, sprite, Deo anything except it say jo we dont have
If user ask for Chochlate then ask him which chocolate
Dairy milk , kitkat, perk , Coconut anything except it say jo we dont have
'''
# Method 1
order = input("select your choice 'colddrinks' or 'chocolates' ")

list_a=['Pepsi', 'fanta', 'sprite', 'Deo']
lis_chocolates =['Dairy milk', 'kitkat', 'perk', 'Coconut']

if order=='colddrinks':
    a = input('which colddrink do you want')

    if a == 'pepsi':
        print('you can get pepsi')
    elif a =='fanta':
        print('you can get fanta')
    elif a =='sprite':
        print('you can get colddrink')
    elif a == 'deo':
        print('you can get colddrink')
    else:
        print('We dont have colddrink')
elif order == 'chocolates':
    b = input('which chocolates do you want')
    if b =='dairymilk':
        print('you can get dairymilk')
    elif b == 'kitkat':
        print('you can get kitkat')
    elif b == 'perk':
        print('you can get perk')
    elif b == ' coconut':
        print('you can get coconut')
    else:
        print('We dont have chocolates')
else:
    print('invalid choice')

'''
Method 2
order = input("select your choice 'colddrinks' or 'chocolates' ")

list_a=['pepsi', 'fanta', 'sprite', 'Deo']
list_b =['Dairy milk', 'kitkat', 'perk', 'Coconut']

if order =='colddrinks':
   cl = input('which colddrink do you want')
   if cl in list_a:
        print('you can get',cl, 'colddrink')
   else:
       print('we dont have coldrinks')

elif order == 'chocolates':
    b = input('which chocolates do you want')
    if b in list_b:
        print('you can get', b, 'chocolate')
    else:
        print('We dont have chocolates')
else:
    print('invalid choice')
'''




