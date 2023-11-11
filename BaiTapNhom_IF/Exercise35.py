HumanYear=int(input('Enter human year: '))
if HumanYear<0:
    print("Error")
else:
    if HumanYear<=2:
        DogYear=HumanYear*10.5
    else:
        DogYear=2*10.5+(HumanYear-2)*4
    print(DogYear," correspond to ",HumanYear,' human year: ',sep='')