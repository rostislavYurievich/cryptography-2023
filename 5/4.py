import hashlib
from hashbase import RIPEMD320, RIPEMD128, RIPEMD256

def open_big(path):
    with open(path) as f:
        data = f.readlines()
    return data
data = open_big('D:\Kirill\Documents/banana.txt')
a = ''.join(data)

print(f"2) RIPEMD-320  {RIPEMD320().generate_hash(a)}")
print('3) MD5 ', (hashlib.md5(a.encode()).hexdigest()).upper())
print('4) SHA-256 ', (hashlib.sha256(a.encode()).hexdigest()).upper())
print(f"5) RIPEMD-128  {RIPEMD128().generate_hash(a)}")
print('6) RIPEMD–160 ', hashlib.new("ripemd160", a.encode()).hexdigest())
print('7) SHA-512 ', (hashlib.sha512(a.encode()).hexdigest()).upper())
print('8) SHA-384 ', (hashlib.sha384(a.encode()).hexdigest()).upper())
print(f"9) RIPEMD-256  {RIPEMD256().generate_hash(a)}")
print('10) SHA-224 ', (hashlib.sha224(a.encode()).hexdigest()).upper())
