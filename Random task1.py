import random
r = random.randint(0, 16777215)
color = format(r, 'x')
color = '#'+color
print('Random Hex Color is :', color)

alpha = ["a", "b", "c", "d", "e", 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', "z"]
random_alpha = random.choice(alpha)
print(f'Random Alphabetic word : {random_alpha}')


random_value = random.randint(100, 199)
print(f'Number between two values is : {random_value}')


random_range = random.randrange(0, 70, 7)
print(f'Random range between 0 to 70 is: {random_range}')
