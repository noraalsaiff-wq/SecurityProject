# CaesarCipher.py
# Caesar (shift) cipher: encryption and decryption


def shift_text(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha() and ch.isascii():
            # pick the starting point depending on upper/lower case
            base = ord('A') if ch.isupper() else ord('a')
            # shift the letter and wrap around the alphabet using mod 26
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            # spaces, numbers and symbols stay the same
            result += ch

    return result


def encrypt(plaintext, key):
    # C = (P + key) mod 26
    return shift_text(plaintext, key)


def decrypt(ciphertext, key):
    # P = (C - key) mod 26
    return shift_text(ciphertext, -key)


# quick test
if __name__ == "__main__":
    c = encrypt("Hello World", 3)
    print(c)                # Khoor Zruog
    print(decrypt(c, 3))    # Hello World
