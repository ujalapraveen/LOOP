r=1
while r<=3:
	c=1
	while c<=3	:
		if(c==1)or(c==3)or (r==1 and c!=1 and c!=3) or (r==3 and c!=1 and c!=3):
			print('*',end='' '')
		else:
			print('' '',end=' ')
		c=c+1
	print()
	r=r+1

# ANOTHER METHOD SQAURE PRINT

# r=1
# while r<=3:
# 	c=1
# 	while c<=3:
# 		if c==1 or c==3or r==1 or r==3 :
# 			print('*',end='' '')
# 		else:
# 			print('' '',end=' ')
# 		c=c+1
# 	print()
# 	r=r+1
