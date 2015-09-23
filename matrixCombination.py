import itertools
m=input("Enter number of rows: ")
#initialize blank list of m rows and any number of columns
d=[[] for x in xrange(0,m)]
i=0
c=[]
# Code block to fill in the values
while i< len(d):
    a=input("Enter row 1 values eg if the values are 1,2,3 enter 123: ")
    b=str(a)
    i=i+1
    e=[]
    for digits in b:
        e.append(int(digits))
    c.append(e)
    #start the combination from bottom to top
    finalList=c[::-1]
for element in itertools.product(*finalList):
    print element
