import random
import sympy
import math
<<<<<<< HEAD
# Функция для проверки на простоту
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

# Функция для нахождения обратного модуля
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Генерация ключей
def generate_keys(bit_length):
    # Генерация случайных простых чисел p и q
    p = sympy.randprime(2 ** (bit_length - 1), 2 ** bit_length - 1)
    q = sympy.randprime(2 ** (bit_length - 1), 2 ** bit_length - 1)
=======

# Генерация ключей
def generate_keys():
    # Генерация случайных простых чисел p и q
    p = sympy.randprime(1,1000)
    q = sympy.randprime(1,1000)
>>>>>>> branch_1

    n = p * q
    phi = (p - 1) * (q - 1)

<<<<<<< HEAD
    e = 65537  # Обычно выбирают фиксированное значение для e

    # Нахождение обратного модуля для e
    d = mod_inverse(e, phi)
=======
    e = 2
    while (math.gcd(e,phi)!=1):
        e = sympy.randprime(1,phi-1)
    d = (k*phi(n) + 1)/e
>>>>>>> branch_1
    return ((e, n), (d, n))

# Шифрование
def encrypt(public_key, plaintext):
    e, n = public_key
<<<<<<< HEAD
    cipher_text = [pow(ord(char), e, n) for char in plaintext]
    return cipher_text
=======
    return [pow(ord(char), e)%n for char in plaintext]
>>>>>>> branch_1

# Дешифрование
def decrypt(private_key, cipher_text):
    d, n = private_key
<<<<<<< HEAD
    plain_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain_text)

bit_length = 256  # Длина ключа в битах

# Генерация ключей
public_key, private_key = generate_keys(bit_length)
=======
    return ''.join([chr(pow(char, d)%n) for char in cipher_text])


# Генерация ключей
public_key, private_key = generate_keys()
>>>>>>> branch_1

# Сообщение для шифрования
message = "Hello, RSA!"

# Шифрование сообщения
encrypted_message = encrypt(public_key, message)
print("Зашифрованное сообщение:", encrypted_message)

# Дешифрование сообщения
decrypted_message = decrypt(private_key, encrypted_message)
print("Расшифрованное сообщение:", decrypted_message)
