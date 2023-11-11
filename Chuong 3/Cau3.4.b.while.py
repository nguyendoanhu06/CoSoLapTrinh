# i=1
# while i<=17:
#     j=1
#     while j<=i:
#         print('*', end='')
#         j=j+1
#     print('' )
#     i=i+2

n=9
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range((2*i)-1):
        print("*",end="")
    print()