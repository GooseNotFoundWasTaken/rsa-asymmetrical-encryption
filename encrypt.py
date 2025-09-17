from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import os

def convert_string_to_numbers(string):
    b = []
    num = 0
    for char in string:
        b.append(int(format(ord(char), '08b'), 2))
    for i, byte in enumerate(b):
        num += byte * (256 ** (len(b) - (i + 1)))
    return num

fileToEncrypt = input("File to encrypt: ")

folder = input("Who are you encrypting this message for?: ")

input("Are you sure you want to encrypt this file? It's original contents will be wiped and cannot be retreived without the private key (which you shouldn't have).\nPress Enter to continute or ctrl+c to exit.")

with open(fileToEncrypt, 'r') as file:
    
    data = file.read().encode('utf-8')
    
    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CTR)  

    ciphertext = cipher.encrypt(data)

    nonce = cipher.nonce

print("Reading public key...")

with open(f"contacts/{folder}/rsakey.public", 'r') as file:
    data = file.read().split(", ")
    n, e = int(data[0]), int(data[1])
    encryptedKey = pow(convert_string_to_numbers(str(key)), e, n)

print(f"Public key accepted! Replacing '{fileToEncrypt}' with encrypted message.)")

os.remove(fileToEncrypt)

with open(f"{fileToEncrypt}", 'w') as file:
    
    file.writelines(f"{convert_string_to_numbers(str(ciphertext))}, {encryptedKey}, {convert_string_to_numbers(str(nonce))}")

input("Press Enter to Exit.")