# Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)


num=int(input('enter a number'))
a=num
sum=0
while a>0:
	digit=a%10
	sum=sum+digit**3
	a=a//10
if num==sum:
	print('armstrong no')
else:
	print('not armstrong no')