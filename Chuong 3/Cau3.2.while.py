# n=int(input())
# i=1
# while i<=n:
#     print(i,end=' ')
#     if i%10==0:
#         print('')
#     i=i+1

n=int(input())
for i in range (1,n+1,1):
    print(i,end=' ')
    if i%10==0:
        print('')
