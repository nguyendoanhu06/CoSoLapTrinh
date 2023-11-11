Decibel=float(input("Enter decibel level: "))
if (0<Decibel<40):
    print("Decibel level is lower then the sound of a Quiet room ")
elif Decibel==40:
    print("Decibel level is Quiet room ")
elif (40<Decibel<70):
    print("Decibel level is between the sound of Quiet room and Alarm clock")
elif Decibel==70:
    print("Decibel level is Alarm clock")
elif (70<Decibel<106):
    print("Decibel level is between the sound of Alarm clock and Gas lawnmower ")
elif Decibel==106:
    print("Decibel level is Gas lawnmover")
elif (106<Decibel<130):
    print("Decibel level is between the sound of Gas lawnmower and Jackhammer")
elif Decibel==130:
    print("Decibel level is Jackhammer")
elif Decibel>130 :
    print("Decibel level is higher then the sound of a Jackhammer")
else :
    print("Wrong")