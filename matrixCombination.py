import itertools
m=input("rows ")
d = [[] for x in xrange(0,m)]
columns=zip(*d)
i = 0
c = []
while i < len(d):
	a = input("Enter no ")
	b = str(a)
	i=i+1
	e = []
	for digit in b:
    		e.append (int(digit))
	c.append (e)
	finalList=c[::-1]
for element in itertools.product(*finalList):
    print element
