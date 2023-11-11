n=int(input())
gt=1
i=1
while i<=n:
    n=int(input())
    gt=gt*i
    i=i+1
    if n<0: break
print(gt,sep="",end="")  