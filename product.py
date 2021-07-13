# Write a program to find the product of the digits of a number accepted from the user.


num=int(input("enter a num"))
pro=1
while num>0:
    pro=pro*(num%10)
    num=num//10

print("The product of digits is:",pro)

