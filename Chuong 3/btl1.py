yrsOfService=int(input('yrsOfServiece = '))
salary=int(input('salary = '))
if yrsOfService <5:
    if salary < 500:
        bonus=100
    else:
        bonus=200
else:
    bonus=700
print('Bonus amount:', bonus)