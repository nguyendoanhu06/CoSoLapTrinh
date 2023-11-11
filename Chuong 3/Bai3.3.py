x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+' or ch=='-' or ch=='*' or ch=='/':
    if ch=='+':
        S=x+y
        print(x,'+',y,'=',round(S,1),sep='')
    elif ch=='-':
        S=x-y
        print(x,'-',y,'=',round(S,1),sep='')
    elif ch=='*':
        S=x*y
        print(x,'*',y,'=',round(S,1),sep='')
    elif ch=='/':
        if y==0:
            print('Khong hop le')
        else:
            S=x/y
            print(x,'/',y,'=',round(S,1),sep='')
else:
    print('Khong hop le')