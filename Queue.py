import random
random.seed(5)

# random()	Returns a random float number between 0 and 1
r=random.random()
print(r)
print('=======================')
# seed()	Initialize the random number generator

# randrange()	Returns a random number between the given range
randomRange= random.randrange(1,10,2)
print(f'Rnadom Range 1 to 10 having step value is 2 : "{randomRange}" ')
print('=======================')
# randint()	Returns a random number between the given range
randomInt= random.randint(10,190)
print(f'Rnadom Range 10 to 190  : "{randomInt}" ')

# choice()	Returns a random element from the given sequence
l=['mehak','ali','komal']
l2=[1,2,34,3,445,8,99]
l3=['pop']
random.choice(l)
print(f'Choice from l  : "{random.choice(l)}" ')
print(f'Choice from l2  : "{random.choice(l2)}" ')
print(f'Choice from l  : "{random.choice(l3)}" ')

# choices()	Returns a list with a random selection from the given sequence
print('============= choices')
print(random.choices(l,weights=[7,2,1],k=10))
print('=================================')

# shuffle()	Takes a sequence and returns the sequence in a random order

#l=['mehak','ali','komal']
random.shuffle(l)
print(l)

# sample()	Returns a given sample of a sequence
print(random.sample(l, k=2))

# uniform()	Returns a random float number between two given parameters
print(random.uniform(20, 60))