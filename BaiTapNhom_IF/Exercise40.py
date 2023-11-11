print("Enter the lengths of the 3 sides of the triangle:")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>0 and b>0 and c>0:
    if a==b==c:
        print("Equilateral triangle")
    elif a == b or b ==c or c == a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print('Wrong')