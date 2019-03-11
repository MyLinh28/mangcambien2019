def timx(a,x):
	d=0
	for i in range(len(a)):
		if (a[i]==x):
			d=d+1;
	if d==0:
		print ('chuoi khong co gia tri x')
	else:
		print ('so phan tu co gia tri bang x la: %d' %d)
def sapxep(a):
	for i in range(len(a)):
		for j in range(i+1,len(a)):
			if a[i]>a[j]:
				t=a[i]
				a[i]=a[j]
				a[j]=t
	print(a)
def max(a):
	max=a[0]
	for i in range(len(a)):
		if (a[i]>max):
			max=a[i]
	print ('max=%d'%max)
def mang(a):
	for i in range(len(a)):
		print (a[i]),
def giaithua(x):
	if (x<2):
		return 1
	else:
		return x*giaithua(x-1)
