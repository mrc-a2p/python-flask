def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
         return True 
    
    return False




def palindrome(word):
    reserved_letters = []
    
    for letter in word: 
        reserved_letters.insert(0, letter)


    reversed_word = "".join(reserved_letters)

    if reversed_word == word:
        return True 
    
    return False 


if __name__ == "__main__":
    word = str(input("Escribe una palabra:"))

    result =  palindrome2(word)   

    if result is True:
        print ("{}Si es un palindromo.".format(word ))
    else: 
        print("No es un palindromo.".format(word))   