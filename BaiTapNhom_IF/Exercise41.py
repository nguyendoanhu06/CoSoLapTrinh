C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
letter=input('Enter letter: ')
octave=int(input('Enter octave: '))
if 0<=octave<=8:
    if letter == "A" :
        note = A4
    elif letter == "B" :
        note = B4
    elif letter == "C" :
        note = C4
    elif letter == "D" :
        note = D4
    elif letter == "E" :
        note = E4
    elif letter == "F" :
        note = F4
    elif letter == "G" :
        note = G4
    else:
        print("Wrong")
    frequency = note / 2 ** (4 - octave)
    print("Frequency:",frequency)
else:
    print("Wrong")

 