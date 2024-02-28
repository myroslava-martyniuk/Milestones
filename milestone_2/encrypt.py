def encrypt_message(message,key):
    encrypted = ""
    
    for i in range(len(message)):
        char = message[i]

        if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 122):
            encrypted += char
            continue
               
        elif (char.isupper()):
            encrypted += chr((ord(char) + key-65) % 26 + 65)
                
        else:
            encrypted += chr((ord(char) + key-97) % 26 + 97)
    
    return encrypted

message = input("Give me message to encrypt: ") #The quick brown fox jumps over the lazy dog.
n = int(input("Give me key: "))

print("Here's your encrypted message: " + encrypt_message(message,n))
