# Write a program to check whether a number is prime or not.

num=int(input("enter a num ="))
i=1
c=0
while i <=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print("prime no")
else:
    print("not prime no")

# prime no using braek

# num=int(input('enter a num'))
# count=0
# i=2
# while i<num:
# 	if num%i==0:
# 		count=count+1
# 		break
# 	i=i+1
	
# if count==1:
# 	print(' it is not prime')
# else:
# 	print('it is prime')
