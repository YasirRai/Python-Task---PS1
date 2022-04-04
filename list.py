a=[1,2,34,55,66]
b=[33,4]
a.insert(2,b)
print(a)

list = ['Peter', 'Joseph', 'Ricky', 'Devansh']
for i in range(len(list)):
    print("Hello", list[i])


# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(0, rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("1", end='')
    print()


def fact (n) :
    if n== term +1 :
        return 1
    else :
        return n*fact(n+1)
term = int(input("Enter the term :-"))
print("Factorial =",fact(1))