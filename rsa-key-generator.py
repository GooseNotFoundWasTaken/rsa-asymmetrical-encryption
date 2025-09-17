import sympy
import random
import math

def generateKeys(digits):
    p = sympy.randprime((10 ** (digits - 1)), 10 ** (digits))
    q = p
    while q == p:
        q = sympy.randprime((10 ** (digits - 1)), 10 ** (digits))
    phi = (p - 1) * (q - 1)
    n = p * q
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
        if math.gcd(e, phi) != 1:
            e = 5
            if math.gcd(e, phi) != 1:
                e = 17
                if math.gcd(e, phi) != 1:
                    e = 257
                    if math.gcd(e, phi) != 1:
                        generateKeys(digits)
    return p, q, n, e

print("Generating keys...")

p, q, n, e = generateKeys(600)

r = (p - 1) * (q - 1)

# private exponent
d = pow(e, -1, r)

print("Writing to file...")

with open("rsakey.public", "w") as file:
    file.write(f"{n}, {e}")
with open("rsakey.private", "w") as file:
    file.write(f"{n}, {d}")

print("Done!")

input("Press Enter to exit.")