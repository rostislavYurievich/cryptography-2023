import random
import sympy
import math

# Генерация ключей
def generate_keys():
    # Генерация случайных простых чисел p и q
    p = sympy.randprime(1,1000)
    q = sympy.randprime(1,1000)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while (math.gcd(e,phi)!=1):
        e = sympy.randprime(1,phi-1)
    d = (k*phi(n) + 1)/e
    return ((e, n), (d, n))

# Шифрование
def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e)%n for char in plaintext]

# Дешифрование
def decrypt(private_key, cipher_text):
    d, n = private_key
    return ''.join([chr(pow(char, d)%n) for char in cipher_text])


# Генерация ключей
public_key, private_key = generate_keys()

# Сообщение для шифрования
message = "Hello, RSA!"

# Шифрование сообщения
encrypted_message = encrypt(public_key, message)
print("Зашифрованное сообщение:", encrypted_message)

# Дешифрование сообщения
decrypted_message = decrypt(private_key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
