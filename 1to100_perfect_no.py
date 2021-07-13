i=1
while i<=100:
    sum=0
    j=1
    while j<i:
        if i%j==0:
            sum+=j
        j+=1
    if sum==i:
        print(i,"perfect no")
        
    i+=1
