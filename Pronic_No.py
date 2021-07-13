num=int(input("enter a no"))
i=0
c=0
while i <num:
    if i*(i+1)==num:
        c=1
    i+=1
if c==1:
    print("pronic no")
else:
    print("not pronic no")