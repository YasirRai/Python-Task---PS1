import random
random.seed(1)
names = ['Abdul Muhaimin', 'Ali', 'Hammad', 'farhan', 'Rehan', 'Nazal', 'yasir']
for x in names:
    score = random.randint(60, 90)
    print(x, "your score is", score)
