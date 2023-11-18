bit = input("Enter an 8-bit string: ")

while bit: 
    if len(bit) != 8 or not bit.isdigit():  
        print("Error: Incorrect format")
    else:
        count_one = bit.count('1')  
        
        if count_one % 2 == 0:  
            print("The even parity bit will be 0")
        else: 
            print("The even parity bit will be 1")
    
    bit = input("Enter an 8-bit string: ")  

print("End of the program")