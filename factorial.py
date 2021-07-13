# Write a program to print the factorial of a number accepted by the user.

i=int(input('enter a number'))
factor=1
while i>0:
		factor= factor*i
		i=i-1
print('Factorial=',factor)