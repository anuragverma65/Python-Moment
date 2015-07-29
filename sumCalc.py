a = input("choose the starting number\n")
b= input("choose the end\n")
c=reduce(lambda x, y: x+y, range(a,b))
print "the sum of these given range is "+str(c)

