BinaryNumber=int(input("Enter the binary number: "))
DecimalNumber = 0
i = 1
while BinaryNumber!=0:
    a = BinaryNumber%10
    DecimalNumber = DecimalNumber + (a*i)
    i = i*2
    BinaryNumber = int(BinaryNumber/10)

print("The decimal number is:", DecimalNumber)