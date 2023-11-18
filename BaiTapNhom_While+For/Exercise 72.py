string = input("Please enter a string: ")
palindrome = True
i =  0
while i < len (string) / 2 and palindrome:
   if string[i] != string[len (string) - i - 1]:
      palindrome = False
   i =  i + 1
if  palindrome:
   print (string,  "string is a palindrome")
else :
   print (string,  "string isn't a palindrome")