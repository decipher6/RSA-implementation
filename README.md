# RSA Encryption and Decryption

This project is a simple implementation of the RSA encryption algorithm, written in Python. It demonstrates RSA key generation, encryption, and decryption by allowing you to encrypt a message with a public key and decrypt it back with a private key.

## Overview

RSA is a widely-used asymmetric cryptographic algorithm that ensures secure communication. This program uses two large prime numbers to generate public and private keys, which can then be used to encrypt and decrypt messages.

## How It Works

1. **Key Generation**:
   - Generate two distinct prime numbers `p` and `q`.
   - Compute `n = p * q` (modulus) and `phi = (p - 1) * (q - 1)`.
   - Choose an integer `e` (public exponent) that is coprime with `phi`.
   - Calculate the modular inverse `d` of `e` with respect to `phi`, resulting in the private exponent.
   - Public key: `(e, n)` and Private key: `(d, n)`.

2. **Encryption**:
   - Encrypt each character in the message using the formula: `ciphertext = (ord(char) ** e) % n`.

3. **Decryption**:
   - Decrypt each character using the formula: `plaintext = chr((char ** d) % n)`.

## Requirements

- Python 3.x
- [sympy](https://www.sympy.org/en/index.html) library for generating random prime numbers.

Install `sympy` with:

```bash
pip install sympy
