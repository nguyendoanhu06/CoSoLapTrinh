sum = 0
count = 0

value = float(input("Enter a value (or enter 0 to finish): "))

if value == 0:
    print("Error: The first value cannot be 0.")
else:
    while value != 0:
        sum += value
        count += 1
        value = float(input("Enter a value (or enter 0 to finish): "))

    average = sum / count if count > 0 else 0
    print("The average of the values is:", average)