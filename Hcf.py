num=int(input('enter a num'))
num2=int(input('enter a num'))
if num>num2:
		m=num
else:
		m=num2
i=1
while i<=m:
    if num%i==0 and num2%i==0:
        hcf=i
        i=i+1
print('Hcf=',hcf)