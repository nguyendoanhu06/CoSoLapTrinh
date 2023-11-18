def is_multiple_word_palindrome(s):
    n = len(s)
    i, j = 0, n - 1
    while i < j: 
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
        
    return True

if __name__ == "__main__":
    print("Enter a string: ", end=' ') 
    s = input()
    result = is_multiple_word_palindrome(s) 
    if result:
        print("{} is palindrome.".format(s)) 
    else:
        print("{} is not palindrome.".format(s))