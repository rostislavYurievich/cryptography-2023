import random
import sympy
import math

# Генерация ключей
def generate_keys():
    # Генерация случайных простых чисел p и q
    p = sympy.randprime(1,30)
    q = sympy.randprime(1,30)

    n = p * q
    e = 2
    phi = (p - 1) * (q - 1)
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e+=1
    k = 2 #целочисленая константа
    d = int((1 + (k * phi)) / e)
    return ((e, n), (d, n))

# Шифрование
def encrypt(public_key, msg):
    e, n = public_key
    a = []
    for i in msg:
        a.append(pow(i,e,n))
    return a
    

# Дешифрование
def decrypt(private_key, msg):
    d, n = private_key
    a = []
    for i in msg:
        a.append(pow(i,d,n))
    return a


# Генерация ключей
public_key, private_key = generate_keys()

message = [1,3,3,4,5]

# Шифрование сообщения
encrypted_message = encrypt(public_key, message)
print("Зашифрованное сообщение:", encrypted_message)

# Дешифрование сообщения
print("Расшифрованное сообщение:", decrypt(private_key, encrypted_message))
