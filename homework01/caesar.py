def encrypt_caesar(plaintext: str) -> str:
    for i in range (len(plaintext)):
        znach=ord(plaintext[i])
        if znach >= 65 and znach <= 87 or znach >= 97 and znach <= 119:
            znach += 3
        elif znach >= 88 and znach <= 90 or znach >= 119 and znach <= 122:
            znach -= 23
        print(chr(znach), end='')
    return chr(32)
        
slovodliakod=str(input())
print(encrypt_caesar(slovodliakod))


#encrypt_caesar("PYTHON") выводит на экран "SBWKRQ"
#encrypt_caesar("python") выводит на экран "sbwkrq"
#encrypt_caesar("Python3.6") выводит на экран "Sbwkrq3.6"
#encrypt_caesar("") выводит на экран ""




def decrypt_caesar(ciphertext: str) -> str:
    for i in range (len(ciphertext)):
        znach=ord(ciphertext[i])
        if znach >= 68 and znach <= 90 or znach >= 100 and znach <= 122:
            znach -= 3
        elif znach >= 65 and znach <= 67 or znach >= 97 and znach <= 99:
            znach += 23
        print(chr(znach), end='')
    return chr(32)
    

zacodslovodliarazkod=str(input())
print(decrypt_caesar(zacodslovodliarazkod))



#decrypt_caesar("SBWKRQ") выводит на экран "PYTHON"
#decrypt_caesar("sbwkrq") выводит на экран "python"
#decrypt_caesar("Sbwkrq3.6") выводит на экран "Python3.6"
#decrypt_caesar("") выводит на экран ""