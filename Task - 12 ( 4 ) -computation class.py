import math


class computation:
    def __int__(self):
        print("Skillevetion Python Task")

    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print(fact)

    def sum(self):
        self.n = [1, 2, 3, 4, 5, 6]
        m = math.fsum(self.n)
        print(m)

    def testprim(self, num):
        if num >= 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    #                                                            print(i, "times", num // i, "is", num)
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is negative number ")

    def testprims(self, a, b):

        number = 0
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                number = number + 1
        if number == 1:
            print("The numbers", a, "and", b, "are co-primes")
        else:
            print("The numbers", a, "and", b, "are not co-primes")

    def tableMult(self, n):

        for i in range(1, 11):
            print(str(n) + " x " + str(i) + " = " + str(n * i))

    def allTablesMult(self):
        for j in range(1, 10):
            print("the multiplication table of:", j, "is:")
            for i in range(1, 10):
                print(i, "x", j, "=", i * j)

    def listDiv(self, n):

        lDiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                lDiv.append(i)
        print(lDiv)

    def listDivPrim(self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range(1, n + 1):
            if n % i == 0 and self.testprim(i):
                lDiv.append(i)
        return lDiv


com = computation()
com.factorial(3)
com.sum()
com.testprim(9)
com.testprims(21, 5)
com.tableMult(3)
com.allTablesMult()

com.listDiv(18)
com.listDivPrim(18)
