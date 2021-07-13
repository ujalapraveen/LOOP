num=int(input('enter a no ='))
sum=0
i=1
while i<num:
	if num%i==0:
		sum=sum+i
	i=i+1
if num==sum:
	print('perfect no')
else:
		print('not perfect')