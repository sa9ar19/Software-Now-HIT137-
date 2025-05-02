"""
Question 1
Create a program that reads the text file “raw_text.txt” , encrypts its contents using a
simple encryption method, and writes the encrypted text to a new file “encrypted_text.txt”. 
Then create a function to decrypt the content, and a function to check the correctness 
of decrypted text.

Requirements
The encryption should take two user inputs (n, m), and follow these rules:
• For lowercase letters:
    o If the letter is in first half of alphabet (a-m): shift forward by n * m
    o If the letter is in second half (n-z): shift backward by n + m
• For uppercase letters:
    o If the letter is in first half (A-M): shift backward by n
    o If the letter is in second half (N-Z): shift forward by m^2
• Special characters, and numbers remain unchanged.
"""

import random 

### Function to encrypt plain text ###
def encrypt(text, m, n):
    
    cipherText = ""

    for ch in text:
        if "a" <= ch <= "m":
            shift = m * n
            cipherText += chr((ord(ch) - ord("a") + shift)%13 + ord("a"))
        elif "n" <= ch <= "z": 
            shift = m + n
            cipherText += chr((ord(ch) - ord("n") - shift)%13 + ord("n"))
        elif "A" <= ch <= "M":
            shift = n
            cipherText += chr((ord(ch) - ord("A") - shift)%13 + ord("A"))
        elif "N" <= ch <= "Z":
            shift = pow(m, 2)
            cipherText += chr((ord(ch) - ord("N") + shift)%13 + ord("N"))
        else: 
            cipherText += ch
            
    return cipherText


### Function to decrypt ciphertext ###
def decrypt(text, m, n):
    
    decryptedText = ""
    
    for ch in text:
        if "a" <= ch <= "m" : 
            shift = m * n
            decryptedText += chr((ord(ch) - ord("a") - shift)%13 + ord("a")) 
        elif "n" <= ch <= "z": 
            shift = m + n
            decryptedText += chr((ord(ch) - ord("n") + shift)%13 + ord("n"))
        elif "A" <= ch <= "M":
            shift = n
            decryptedText += chr((ord(ch) - ord("A") + shift)%13 + ord("A"))
        elif "N" <= ch <= "Z":
            shift = pow(m, 2)
            decryptedText += chr((ord(ch) - ord("N") - shift)%13 + ord("N"))
        else: 
            decryptedText += ch
    
    return decryptedText


### Function to check if the decrypted text matches the plain text ###
def check(text1, text2):
   return text1 == text2
        
# open the files 
fileOne = open("raw_text.txt","r")     
fileTwo = open("encrypted_text.txt","w")


# read the "raw_text.txt" file 
plainText = fileOne.read()
print("Plain text from the file: ",plainText)


# take two values(m, n) from the user
shiftValue1 = int(input("Enter a shift value: "))
shiftValue2 = int(input("Enter another shift value: "))


# encrypt the text in the file using encrypt() Function
encryptedText = encrypt(plainText, shiftValue1, shiftValue2)
print("Encrypted text: ", encryptedText)

# write the encrypted text to a new file “encrypted_text.txt”.
fileTwo.write(encryptedText)
fileTwo.close()

# decrypt the cipher text using decrypt() Function
decryptedText = decrypt(encryptedText, shiftValue1, shiftValue2)
print("Decrypted Text: ", decryptedText)

# check the correctness of the program using check() function
if check(plainText, decryptedText):
    print("\n Decryption successful!")
else:
    print("\n Decryption Unsuccessful !!!!! ")