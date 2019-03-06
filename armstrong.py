n=int(input("enter  the number:"))
sum=0
num=n
while(n>0):
	r=n%10
	sum=sum+r**3
	n=n/10
if(sum==num):
	print("Given number is a Armstrong")
else:
print("Given number is not a Armstrong")
