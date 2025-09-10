def convert_string_to_numbers(string):
    b = []
    num = 0
    for char in string:
        b.append(int(format(ord(char), '08b'), 2))
    for i, byte in enumerate(b):
        num += byte * (256 ** (len(b) - (i + 1)))
    return num


with open("rsakey.public", 'r') as file:
    data = file.read().split(", ")
    n, e = int(data[0]), int(data[1])

fileToEncrypt = input("File to encrypt: ")

with open(fileToEncrypt, 'r') as file:
    data = convert_string_to_numbers(file.read())
    c = pow(data, e, n)

with open(f"{fileToEncrypt}.encrypted", 'w') as file:
    file.writelines(str(c))
