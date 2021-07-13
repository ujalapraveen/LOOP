i=2
a=0
b=0
c=0
while i<=100:
	j=2
	count=0
	while j<i:
		if i%j==0:
			count=count+1
		j=j+1
	if count==0:
		if i%2==0:
			print(i,'even prime no')
			a=a+1
		else:
			print(i,'odd prime no')
			b=b+1
	else:
		print(i,'not prime no')
		c=c+1
	i=i+1					
print(a,'total even prime no')
print(b,'total odd prime no')
print(c,'total not prime no')	
