from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def convert_number_to_string(number):
    n = number
    b = []
    string = ''
    while n > 0:
        b.append(n % 256)
        n = n // 256
    b.reverse()
    for i, byte in enumerate(b):
        b[i] = chr(byte)
    return ''.join(b)

print("Reading private key...")

with open("rsakey.private", 'r') as file:
    data = file.read().split(", ")
    n, d = int(data[0]), int(data[1])

print("Private key accepted!")

fileToDecrypt = input("File to decrypt: ")

with open(fileToDecrypt, 'r') as file:
    data = file.read()
    ciphertext, encryptedKey, nonce = data.split(', ')
    
    nonce = convert_number_to_string(int(nonce))
    nonce = nonce[2:-1]
    nonce = nonce.encode("latin1").decode("unicode_escape").encode("latin1")

    key = convert_number_to_string(pow(int(encryptedKey), d, n))
    key = key[2:-1]
    key = key.encode("latin1").decode("unicode_escape").encode("latin1")

    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)  

    ciphertext = convert_number_to_string(int(ciphertext))
    ciphertext = ciphertext[2:-1]
    ciphertext = ciphertext.encode("latin1").decode("unicode_escape").encode("latin1")

    message = cipher.decrypt(ciphertext)
    
print(f"Writing decrypted content to {fileToDecrypt}.decrypted ")

with open(f"{fileToDecrypt}.decrypted", 'w') as file:
    file.writelines(message.decode())