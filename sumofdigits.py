sumofdigits=0
n=int(input("enter the number:"))
while(n!=0):
	temp=n%10
	sumofdigits=sumofdigits+temp
	n=n/10
print("The sum of digits is :",sumofdigits)
