m1=550
m2=750
m3=950
m4=1350
VAT=0.1
s=int(input('Tieu thu='))
if s>=100:
    a=s-100
    x=s-a
    gia1=m1*x
    if 50<a<=100:
        b=a-50
        y=a-b
        gia2=m2*y
        gia3=m3*b
        print('Phai tra=',(gia1+gia2+gia3)*VAT+(gia1+gia2+gia3), sep='')
    elif a<=50: 
        gia2=m2*a
        print('Phai tra=',(gia1+gia2)*VAT+(gia1+gia2), sep='')
    if a>100:
        b=a-50
        y=a-b
        gia2=m2*y
        if b>50:
            c=b-50
            z=b-c
            gia3=m3*z
            gia4=m4*c
            print('Phai tra=',(gia1+gia2+gia3+gia4)*VAT+(gia1+gia2+gia3+gia4), sep='')
        elif b<=50:
            gia3=b*m3
            print('Phai tra=',(gia1+gia2+gia3)*VAT+(gia1+gia2+gia3), sep='')
else: 
    print('Phai tra=',s*m1, sep='')

