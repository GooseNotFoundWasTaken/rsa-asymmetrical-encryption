with open("rsakey.public", 'r') as file:
    data = file.read().split(", ")
    n, e = int(data[0]), int(data[1])

fileToEncrypt = input("File to encrypt: ")

with open(fileToEncrypt, 'r') as file:
    data = int(file.read())
    c = pow(data, e, n)

with open(f"{fileToEncrypt}.encrypted", 'w') as file:
    file.writelines(str(c))
