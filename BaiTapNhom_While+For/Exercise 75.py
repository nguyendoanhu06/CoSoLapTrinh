m=int(input())
n=int(input())
d=min(m,n)
if  m % d != 0 or  n % d != 0:
    d=d-1
print("greatest common divisor", m,"and", n, "to be", d)