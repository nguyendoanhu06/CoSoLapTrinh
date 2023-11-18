n = int(input("Enter an integer (2 or greater): "))
if n < 2:
    print("Please enter an integer greater than or equal to 2.")
else:
    print(f"The prime factors of {n} are:")
    for factor in range(2, n+1):
        while n % factor == 0:
            print(factor)
            n = n // factor
