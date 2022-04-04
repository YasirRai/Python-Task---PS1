# Create a rolling dice program
import random
dice = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
chance = 0
print("Maximum Try to win this game is '3'")
for i in range(0, 3):                               # to create 3 times chances
    u = input("Press 'd' for rolling the dice ")            # take d from User to dice the roll

    if u == 'd':
        d1 = random.choice(dice)
        d2 = random.choice(dice2)
        if d1 == d2:
            print("dice numbers are equal ", d1, d2)
            chance += 1
            if chance == 3:
                print("You win the game")
        if d1 != d2:
            print("Try Again ", d1, d2)
    else:
        print('wrong Selection ')
if chance != 3:
    print("You reached Maximum tries")
    print("\nSorry ! You Failed .")
