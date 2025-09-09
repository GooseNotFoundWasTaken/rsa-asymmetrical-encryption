with open("rsakey.private", 'r') as file:
    data = file.read().split(", ")
    n, d = int(data[0]), int(data[1])

fileToDecrypt = input("File to decrypt: ")

with open(fileToDecrypt, 'r') as file:
    c = int(file.read())
    message = pow(c, d, n)

with open(f"{fileToDecrypt}.decrypted", 'w') as file:
    file.writelines(str(message))
