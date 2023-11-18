total= 0
while True:
   age = input("Please enter your age: ")
   if age == "":
       break
   else:
       age_int = int(age)
       if age_int <= 2:
           total = total + 0
       elif age_int>=3 and age_int<=12:
           total = total + 14
       elif age_int>=13 and age_int<=64:
           total = total + 23
       else:
           total = total + 18
print('the total amount is:', total)


