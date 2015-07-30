a = input("enter first number\n")
b= input("choose second number\n")
limit=[]
limit.append(a)
limit.append(b)
natNo=range(1,1000)
xyz = []
for i in limit:
	xyz +=filter(lambda x: x == i or x % i==0, natNo)	
set = {}
map(set.__setitem__, xyz, [])
nums=set.keys()
print "the multiples of the given numbers are: "+str(nums)
c=reduce(lambda x, y:x+y, nums)
print "the sum of the multiples of the given numbers is "+str(c)
