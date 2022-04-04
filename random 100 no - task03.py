import random
no = []
a = 1

for i in range(1, 100):
    num = random.randint(1, 100)
    no.append(num)

for i in no:
    print('Frequency of', i, ':', no.count(i))

print("Random Number list is ", no)

