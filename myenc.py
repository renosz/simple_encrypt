import base64, time, sys, os, zlib
from hashlib import md5

os.system('cls' if os.name == 'nt' else 'clear')
print("""===========================================
Simple My Encrypted Password Using Base64
returning to (
    mainPassword,
    fullEncryptedPassword,
    realPassword
)
.> Rensmt
===========================================""")
passwd = input("Your password: ")

def Encrypt(passwd):
    e1 = base64.b85encode(passwd.encode())
    e2 = base64.b64encode(e1)
    e3 = base64.b32encode(e2)
    enc_pass = f"{e1.decode()[:4]}{e2.decode()[:4]}{e3.decode()[:4]}"
    dec_pass = Decrypt(e3)
    return enc_pass, e3.decode(), dec_pass
def Decrypt(passwd_bytes):
    e3 = base64.b32decode(passwd_bytes)
    e2 = base64.b64decode(e3)
    e1 = base64.b85decode(e2)
    return e1.decode()

mp, fep, rp = Encrypt(passwd) #Split
print("Encrypted Password: ", Encrypt(passwd))
print("Decrypted Password: ", Decrypt(fep.encode()))