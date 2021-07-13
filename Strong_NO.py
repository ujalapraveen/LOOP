num=int(input('enter a no'))
a=num
sum=0
while num>0:
	i=1
	fac=1
	rem=num%10
	while i<=rem:
		fac=fac*i
		i=i+1
	sum=sum+fac
	num=num//10
if sum==a:
	print('num is strog no')
else:
	print('num is not strong no')