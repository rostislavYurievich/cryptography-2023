import hashlib
from hashbase import RIPEMD320, RIPEMD128, RIPEMD256

with open('test2.txt') as f:
    a = ''.join(f.readlines())

print("RIPEMD-320",  RIPEMD320().generate_hash(a))
print("MD5 ", (hashlib.md5(a.encode()).hexdigest()).upper())
print("SHA-256 ", (hashlib.sha256(a.encode()).hexdigest()).upper())
print("RIPEMD-128 ", RIPEMD128().generate_hash(a))
print("RIPEMD–160 ", hashlib.new("ripemd160", a.encode()).hexdigest())
print("SHA-512 ", (hashlib.sha512(a.encode()).hexdigest()).upper())
print("SHA-384 ", (hashlib.sha384(a.encode()).hexdigest()).upper())
print("RIPEMD-256 ", RIPEMD256().generate_hash(a))
print("SHA-224 ", (hashlib.sha224(a.encode()).hexdigest()).upper())

