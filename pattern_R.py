i=1
while i<=6:
	c=1
	while c<=4:
		if c==1 or c==4or i==1 or i==4:
			print(' *',end='')
		else:
			print('   ',end='')
		c=c+1
	print()
	i=i+1	