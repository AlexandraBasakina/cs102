def encrypt_vigenere(plaintext: str, key: str) -> str:
    key_len = len(key)
    plaintext_len = len(plaintext)
    while key_len != plaintext_len:
        key += key
        key_len = len(key)
        if key_len > plaintext_len:
            key = key[:plaintext_len]
            key_len = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        znach = (plaintext_int[i] + key_as_int[i % key_len]) % 26
        ciphertext += chr(znach + 65)
    return ciphertext
    
plaintext=str(input())
key=str(input())
print(encrypt_vigenere(plaintext, key))

#encrypt_vigenere(ATTACKATDAWN, LEMON) выводит на экран LXFOPVEFRNHR




def decrypt_vigenere(ciphertext: str, key: str) -> str:
    key_len = len(key)
    ciphertext_len = len(ciphertext)
    while key_len != ciphertext_len:
        key += key
        key_len = len(key)
        if key_len > ciphertext_len:
            key = key[:ciphertext_len]
            key_len = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        znach = (ciphertext_int[i] - key_as_int[i % key_len]) % 26
        plaintext += chr(znach + 65)
    return plaintext
    
ciphertext=str(input())
key=str(input())
print(decrypt_vigenere(ciphertext, key))

#decrypt_vigenere(LXFOPVEFRNHR, LEMON) выводит на экран ATTACKATDAWN