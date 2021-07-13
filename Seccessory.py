
num=(input("enter a no ="))
i=0
m=0
s=1
while i<len(num):
    if int(num[i])%2==0:
        p=int(num[i])+1
        s=s*p
    i+=1
print(s)