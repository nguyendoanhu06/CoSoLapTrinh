import random

max = random.randint(1, 100)
update = 0

print(max)

count = 1
while count < 100:
    NewNumber = random.randint(1, 100)
    count += 1
    
    print(NewNumber, end=' ')
    
    if NewNumber > max:
        max = NewNumber
        update += 1
        print("<== Update", end=' ')
    print()

print("The maximum value found was", max)
print("The maximum value was updated", update,"time")