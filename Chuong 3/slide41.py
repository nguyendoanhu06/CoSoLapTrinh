n=int(input("n="))
if 0<=n<=100:
    gt=1
    i=1
    while i<=n:
        gt=gt*i
        i=i+1
    
print(n,"!=",gt,sep="")  