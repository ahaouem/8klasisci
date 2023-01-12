from cryptography.fernet import Fernet as fr

#ByBQJFE_OCJU8_1V9nVlbrBjeaqLUyBH-CdksQpWctg=  key
key = "ByBQJFE_OCJU8_1V9nVlbrBjeaqLUyBH-CdksQpWctg="

def encryptMessage(message):
    f = fr(key)
    message = message.encode()
    encryptedMessage = f.encrypt(message)
    return encryptedMessage

def decryptMessage(encryptedMessage):
    f = fr(key)
    decryptedMessage = f.decrypt(encryptedMessage)
    return decryptedMessage.decode()


def encryptFile(filePath, key = key):
    # Create a new Fernet object
    cipher = fr(key)

    # Open the file to encrypt
    with open(filePath, "rb") as fileToEncrypt:
        # Read the contents of the file
        fileData = fileToEncrypt.read()

        # Encrypt the data
        encryptedData = cipher.encrypt(fileData)

    # Overwrite the file with the encrypted data
    with open(filePath, "wb") as fileToEncrypt:
        fileToEncrypt.write(encryptedData)
    return filePath

def decryptFile(filePath, key = key):
    # Create a new Fernet object
    cipher = fr(key)

    # Open the file to decrypt
    with open(filePath, "rb") as fileToDecrypt:
        # Read the contents of the file
        encryptedData = fileToDecrypt.read()

        # Decrypt the data
        decryptedData = cipher.decrypt(encryptedData)

    # Overwrite the file with the decrypted data
    with open(filePath, "wb") as fileToDecrypt:
        fileToDecrypt.write(decryptedData)
    return filePath


#print(encryptFile("./test.txt"))
#print(decryptFile("./test.txt"))

print(decryptFile("./test.txt"))