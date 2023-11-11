# # n=int(input())
# i=1
# while i<=9:
#     j=9
#     while j>=i:
#         print('$', end='')
#         j=j-1
#     print('')
#     i=i+1
n=10
for i in range(1,n):
    for j in range(i-1,9):
        print("$", end="")
    print("")