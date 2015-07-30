primes=range(2,50)
for i in range(2,8):
	primes = filter(lambda x: x == i or x % i, primes)
print primes
