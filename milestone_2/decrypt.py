def decrypt_message(message,key):
    decrypted = ""
    
    for i in range(len(message)):
        char = message[i]

        if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 122):
            decrypted += char
            continue
               
        elif (char.isupper()):
            decrypted += chr((ord(char) - key-65) % 26 + 65)
                
        else:
            decrypted += chr((ord(char) - key-97) % 26 + 97)
    
    return decrypted

message = input("Give me message to decrypt: ") #Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.
n = int(input("Give me key: "))

print("Here's your decrypted message: " + decrypt_message(message,n))