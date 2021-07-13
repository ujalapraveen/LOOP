num=int(input("enter the number: "))
num1=int(input('enter a num1'))
if num>num1:
	m=num
else:
	m=num1
while 1:
	if m%num==0 and m%num1==0:
		print(m)
		break
	m=m+1