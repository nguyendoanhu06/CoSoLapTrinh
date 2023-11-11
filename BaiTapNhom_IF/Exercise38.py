m = int(input('Month: '))
d = 0
if m in [1,3,5,7,8,10,12]:
    d = 31
elif m in [4,6,9,11]:
    d = 30
elif m == 2:
    y = int(input('Year: '))
    if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
        d = 29
    else:
        d = 28
else:
    print('Invalid month')
if d != 0:
    print('That month has', d ,'days')