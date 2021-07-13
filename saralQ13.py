weight=int(input("enter the weight ="))
sum=0
i=0
while i<weight:
    weight2=int(input("enter the weight2 ="))
    sum+=weight2
    average=sum/weight
    i+=1
    print(average)
if average%5==0:
    print("true")
else:
    print("false")
