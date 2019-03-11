def cong(a,b):
        print ('%d' %(a+b))
def tru (a,b):
        print ('%d' %(a-b))
def nhan(a,b):
	print ('%d' %(a*b))
def chia(a,b):
	print ('%f' %(a/b))
def sxtang(a):
	for i in range(len(a)):
		for j in range(i+1,len(a)):
			if(a[i]>a[j]):
				t=a[i]
				a[i]=a[j]
				a[j]=t
	print (a)
def sxgiam(a):
        for i in range(len(a)):
                for j in range(i+1,len(a)):
                        if(a[i]<a[j]):
                                t=a[i]
                                a[i]=a[j]
                                a[j]=t
        print (a)

