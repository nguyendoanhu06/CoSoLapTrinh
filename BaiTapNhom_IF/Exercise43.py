leaders = {
    '$1': 'George Washington',
    '$2': 'Thomas Jefferson',
    '$5': 'Abraham Lincoln',
    '$10': 'Alexander Hamilton',
    '$20': 'Andrew Jackson',
    '$50': 'Ulysses S. Grant',
    '$100': 'Benjamin Franklin'}

denomination = input("Enter the denomination:")

if denomination in leaders:
    print("The person appearing on the banknote",denomination,"is",leaders[denomination])
else:
    print("There is no corresponding denomination")