# Write a program to find the sum of the digits of a number accepted from the user.


num=int(input("enter a num"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("The sum of digits is:",sum)


