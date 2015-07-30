fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print fib
nums=fib(34)
print nums
for i in nums:
	filtered_list = filter(lambda x: x%2==0, nums)
	print filtered_list
	c=reduce(lambda x, y:x+y, filtered_list)
print c



