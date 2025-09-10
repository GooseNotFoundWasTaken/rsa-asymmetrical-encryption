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

with open("rsakey.private", 'r') as file:
    data = file.read().split(", ")
    n, d = int(data[0]), int(data[1])

fileToDecrypt = input("File to decrypt: ")

with open(fileToDecrypt, 'r') as file:
    c = int(file.read())
    message = pow(c, d, n)

with open(f"{fileToDecrypt}.decrypted", 'w') as file:
    file.writelines(convert_number_to_string(message))
