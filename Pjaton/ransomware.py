from cryptography.fernet import Fernet as fr
from time import time, sleep
import os

#ByBQJFE_OCJU8_1V9nVlbrBjeaqLUyBH-CdksQpWctg=  key
key = "ByBQJFE_OCJU8_1V9nVlbrBjeaqLUyBH-CdksQpWctg="

def encryptDecryptMessage(message, option):
    cipher = fr(key)
    if option == "encrypt":
        return cipher.encrypt(message)
    elif option == "decrypt":
        return cipher.decrypt(message)

def encryptDecryptFiles(filePaths, option, count = 0, startTime = time()):
    cipher = fr(key)
    if option == "encrypt":
        print("Starting to encrypt")
        for file in filePaths:
            count += 1
            with open(file, "rb") as fileToEncrypt:
                fileData = fileToEncrypt.read()
                encryptData = cipher.encrypt(fileData)
            with open(file, "wb") as fileToEncrypt:
                fileToEncrypt.write(encryptData)
            print("Number of encrypted files:", count, "/", len(filePaths))
    elif option == "decrypt":
        print("Starting to decrypt")
        for file in filePaths:
            count+=1
            with open(file, "rb") as fileToEncrypt:
                fileData = fileToEncrypt.read()
                encryptData = cipher.decrypt(fileData)
            with open(file, "wb") as fileToEncrypt:
                fileToEncrypt.write(encryptData)
            print("Number of decrypted files:", count, "/", len(filePaths))
    print("It took: ", time() - startTime, "seconds")

def encryptDecryptFolder(folderPath, option, startTime = time(), count = 0):
    cipher = fr(key)
    files = os.listdir(folderPath)
    if option == "encrypt":
        for file in files:
            count += 1
            with open(file, "rb") as fileToEncrypt:
                fileData = fileToEncrypt.read()
                encryptData = cipher.encrypt(fileData)
            with open(file, "wb") as fileToEncrypt:
                fileToEncrypt.write(encryptData)
            print("Number of encrypted files:", count, "/", len(files))
    if option == "decrypt":
        for file in files:
            count += 1
            with open(file, "rb") as fileToEncrypt:
                fileData = fileToEncrypt.read()
                encryptData = cipher.decrypt(fileData)
            with open(file, "wb") as fileToEncrypt:
                fileToEncrypt.write(encryptData)
            print("Number of encrypted files:", count, "/", len(files))
    print("It took:", time() - startTime, "seconds")

files = ["./test.txt", "./test2.txt", "./test3.txt"]
