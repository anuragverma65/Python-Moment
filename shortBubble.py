def bubbleSort(alist):
	exchange=True
        i=len(alist)-1
	while i>0 and exchange:
		exchange=False
                for j in range(i):
			if alist[j]>alist[j+1]:
				exchange=True
				alist[j],alist[j+1]=alist[j+1],alist[j]
		i=i-1
alist=[20,30,40,90,50,60,70,80,100,110]
bubbleSort(alist)
print(alist)
