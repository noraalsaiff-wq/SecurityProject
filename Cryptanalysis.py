# Cryptanalysis.py
# Known-plaintext attack on the Caesar cipher

alphabet = "abcdefghijklmnopqrstuvwxyz"


def find_key(plaintext, ciphertext):
    # the two texts must have the same length
    if len(plaintext) != len(ciphertext):
        return None

    # make everything lowercase to make comparison easy
    plaintext = plaintext.lower()
    ciphertext = ciphertext.lower()

    key = None

    for i in range(len(plaintext)):
        p = plaintext[i]
        c = ciphertext[i]

        if p in alphabet and c in alphabet:
            # key = (cipher position - plain position) mod 26
            shift = (alphabet.index(c) - alphabet.index(p)) % 26

            if key is None:
                key = shift          # first letter gives us the key
            elif key != shift:
                return None          # different shift, so the pair is wrong
        else:
            # spaces, numbers and symbols must stay the same
            if p != c:
                return None

    return key

