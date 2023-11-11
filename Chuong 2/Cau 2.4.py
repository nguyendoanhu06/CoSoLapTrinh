import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
S=(a+b+c)/2
DT=S*(S-a)*(S-b)*(S-c)
DienTich=math.sqrt(DT)
print('Dien tich=', DienTich, sep='')