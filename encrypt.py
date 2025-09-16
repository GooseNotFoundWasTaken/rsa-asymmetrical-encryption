from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def convert_string_to_numbers(string):
    b = []
    num = 0
    for char in string:
        b.append(int(format(ord(char), '08b'), 2))
    for i, byte in enumerate(b):
        num += byte * (256 ** (len(b) - (i + 1)))
    return num

fileToEncrypt = input("File to encrypt: ")

with open(fileToEncrypt, 'r') as file:
    
    data = file.read().encode('utf-8')
    
    key = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CTR)  

    ciphertext = cipher.encrypt(data)

    nonce = cipher.nonce

print("Reading public key...")

with open("rsakey.public", 'r') as file:
    data = file.read().split(", ")
    n, e = int(data[0]), int(data[1])
    encryptedKey = pow(convert_string_to_numbers(str(key)), e, n)

print(f"Public key accepted! Writing encrypted content to {fileToEncrypt}.encrypted")

with open(f"{fileToEncrypt}.encrypted", 'w') as file:
    file.writelines(f"{convert_string_to_numbers(str(ciphertext))}, {encryptedKey}, {convert_string_to_numbers(str(nonce))}")