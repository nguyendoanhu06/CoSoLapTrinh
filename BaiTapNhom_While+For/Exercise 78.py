q=int(input('q='))
result=""
while q>0:
    r=q%2
    result=str(r) + result
    q=q//2
    if q==0: break
print(result)