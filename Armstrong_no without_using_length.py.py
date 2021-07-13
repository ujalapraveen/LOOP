num=int(input('enter a num='))
a=num
sum=0
count=0
while a>0:
	count=count+1
	a=a//10
num=a
while a>0:
	rem=a%10
	sum=sum+(rem**count)
	a=a//10
if num==sum:
	print('armstrong no')
else:
	print('not armstrong no')

