i=1
while i<=100:
	count=0
	j=2
	while j<i:
		if i%j==0:
			count=count+1
			break
		j=j+1
	if count==0:
		print(i)
	i=i+1		
