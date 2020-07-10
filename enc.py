def encrypt(text, n):
        result = ""
        for i in range(len(text)): 
            char = text[i] 
  
            if (char.isupper()): 
                result = result + chr((ord(char) + n - 65) % 26 + 65) 
            elif (not char.isalpha()):
                result = result + char
            else: 
                result = result + chr((ord(char) + n - 97) % 26 + 97) 
  
        return result 

encrypted = encrypt("Superpassword1!", 5)
print(encrypted)
decrypted = encrypt(encrypted, -5)
print(decrypted)