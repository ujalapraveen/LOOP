num=int(input('enter a num'))
i=1
pc=0
sum=0
sum1=0
while 1:
		count=0
		j=2
		while j<=i:
				if i%j==0:
					count=count+1
				j+=1
		if count==1:
			print(i,'prime')
			if i%2==0:
				print('even prime sum')
				sum+=1
			else:
					print('odd prime sum')
					sum1+=1
			pc+=1
		if pc==num:
				break
		i+=1
print(sum)
print(sum1)