print "Enter the matrix in the following format\n[[a11,a12.....,a1n],[a21,a22.....a2n],......,[an1,an2,....ann]]"
print "Ex:[[1,2,3],[4,5,6],[7,8,9]"
a=input("Enter matrix A:")
b=input("Enter matrix B:")
p=len(a)
q=len(a[0])
m=len(b)
n=len(b[0])
c=[]
for i in range(p):
	if(q!=m):
		break
	d=[]
	for j in range(n):
		s=0
		for l in range(m):
			s=s+(a[i][l]*b[l][j])
		d.append(s)
	c.append(d)
if(q!=m):
	print "multiplication can't be done"
else:
print c
