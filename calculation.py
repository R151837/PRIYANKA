def sum(a,b):
	a=a+b
	return a
def sub(a,b):
	if(a>b):
		a=a-b
		return a
	else:
		b=b-a
		return b
def mul(a,b):
	a=a*b
	return a
def div(a,b):
	a=a/b
	return a
def sqr(a):
	x=math.sqrt(a)
	return x
while(True):
	print("Choose the operation you want to perform:" )
	print("\n\t1.addition")
	print("\n\t2.substraction")
	print("\n\t3.multiplication")
	print("\n\t4.division")
	print("\n\t5.square root")
	print("\n\t6.exit")
	choice=int(input("enter the number"))
	if choice==1:
		print("enter any two numbers")
		num1=input("enter the number")
		num2=input("enter the another number")
		s=sum(num1,num2)
		print("the sum is :%s" %s)
	elif choice==2:
		print("enter any two numbers")
		num1=input("enter the number")
		num2=input("enter the another number")
		d=sub(num1,num2)
		print("the difference is :%s" %d)
	elif choice==3:
		print("enter any two numbers")
		num1=input("enter the number")
		num2=input("enter the another number")
		m=mul(num1,num2)
		print("the sum is :%s" %m)
	elif choice==4:
		print("enter any two numbers")
		num1=input("enter the number")
		num2=input("enter the another number")
		di=div(num1,num2)
		print("the division is :%s" %di)
	elif choice==5:
		print("enter the numbers")
		num1=input("enter the number")
		sq=sqr(num1)
		print("the square is :%s" %sq)
	else:
		print("\nyou choose to exit")
break
