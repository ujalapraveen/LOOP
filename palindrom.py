# Write a program to check whether a number is palindrome or not.


num=int(input('enter a number'))
rev=0
a=num
while num>0:
		rev=(rev*10)+num%10
		num=num//10
if a==rev:
	print('palindrom no')
else:
	print('not palindrom no')
