num=int(input('enter a no'))
a=num
sum=0
c=len(str(num))
while a>0:
	digit=a%10
	sum=sum+digit**c
	a=a//10
if num== sum:
	print('armstrong no')
else:
	print('not armstrong no'