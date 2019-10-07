def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    key_len = len(keyword)
    plaintext_len = len(plaintext)
    while key_len != plaintext_len:
        keyword += keyword
        key_len = len(keyword)
        if key_len > plaintext_len:
            keyword = keyword[:plaintext_len]
            key_len = len(keyword)
    if keyword.isupper():
        code_A, code_Z = 65, 90
    else:
        code_A, code_Z = 97, 122
    for ch, k in zip(list(plaintext), list(keyword)):
        if ord(ch) + ord(k) - code_A > code_Z:
            ch = chr((ord(ch)) - 26)
        ciphertext += chr(ord(ch) + (ord(k) - code_A))
    return ciphertext
    

def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    key_len = len(keyword)
    ciphertext_len = len(ciphertext)
    while key_len != ciphertext_len:
        keyword += keyword
        key_len = len(keyword)
        if key_len > ciphertext_len:
            keyword = keyword[:ciphertext_len]
            key_len = len(keyword)
    if keyword.isupper():
        code_A = 65
    else:
        code_A = 97
    for ch, k in zip(list(ciphertext), list(keyword)):
        if (ord(ch) < ord(k)):
            ch = chr(ord(ch) + 26)
        plaintext += chr(ord(ch) - (ord(k) - code_A))
    return plaintext
 