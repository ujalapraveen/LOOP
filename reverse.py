

num=int(input("enter a num"))
i=0
rev=0
while num>0:
    rev=(rev*10)+num%10
    num=num//10
print(rev)



