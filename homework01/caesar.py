def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for ch in plaintext:
        code = ord(ch)
        if 'a' <= ch < 'x' or 'A' <= ch < 'X':
            code += 3
        elif 'x' <= ch <= 'z' or 'X' <= ch <= 'Z':
            code -= 23
        ciphertext += chr(code)
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    for i in range (len(ciphertext)):
        znach=ord(ciphertext[i])
        if znach >= 68 and znach <= 90 or znach >= 100 and znach <= 122:
            znach -= 3
        elif znach >= 65 and znach <= 67 or znach >= 97 and znach <= 99:
            znach += 23
        print(chr(znach), end='')
    return chr(32)
