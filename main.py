import random

# Function to find gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate modular inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

# Function to generate RSA keys
def generate_keys():
    # Two prime numbers (for simplicity, these are hardcoded small primes)
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(1, phi)
    # Ensure e is coprime with phi and 1 < e < phi
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Calculate d
    d = mod_inverse(e, phi)

    # Public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

# RSA encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    encrypted_text = [(ord(char) ** e) % n for char in plaintext]
    return encrypted_text

# RSA decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_text = ''.join([chr((char ** d) % n) for char in ciphertext])
    return decrypted_text

# Driver code
public_key, private_key = generate_keys()
print("Public Key:", public_key)
print("Private Key:", private_key)

# Example message
message = "HELLO"
print("Original Message:", message)

# Encrypting the message
encrypted_message = encrypt(public_key, message)
print("Encrypted Message:", encrypted_message)

# Decrypting the message
decrypted_message = decrypt(private_key, encrypted_message)
print("Decrypted Message:", decrypted_message)
