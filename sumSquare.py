from math import sqrt
nums=range(1,101)
sum=0
for i in nums:
	sum=sum+i
sumSquare=sum*sum
print sum
print sumSquare
num=0
for i in nums:
	num+=i*i
print num
diff=sumSquare-num
print diff
