r=1
while r<=5:
	c=1
	while c<=4:
		if(c==1)or(c==4)or (r==1 and c!=1 and c!=4) or (r==3 and c!=1 and c!=4):
			print('*',end='' '')
		else:
			print('' '',end=' ')
		c=c+1
	print()
	r=r+1


# ANOTHER METHOD A PRINT
# r=1
# while r<=5:
# 	c=1
# 	while c<=4:
# 		if c==1 or c==4or r==1 or r==4 :
# 			print('*',end='' '')
# 		else:
# 			print('' '',end=' ')
# 		c=c+1
# 	print()
# 	r=r+1