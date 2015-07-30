from math import sqrt

factors=[]
a = input("enter number\n")
def primeTest(y):
    if y < 2:
        return False
    for i in range(int(sqrt(y)) + 1)[2:]:
        if y % i == 0:
            return False
    return True

def calcFactors(x):
	for i in range (1,x):
		if (x % i) == 0:
			if primeTest(i):
				factors.append(i)
	print factors

calcFactors(a)
