import random
from itertools import cycle

def generate_one_time_pad_binary(length):
    return ''.join([str(random.randint(0, 1)) for _ in range(length)])


def one_time_pad_binary_encrypt(message, key):
    encrypted = []
    for c,k in zip(message, cycle(key)):
        encrypted_bit = str(int(c) ^ int(k))
        encrypted.append(encrypted_bit)
    return ''.join(encrypted)


def one_time_pad_binary_decrypt(message, key):
    decrypted = []
    for c,k in zip(message, cycle(key)):
        decrypted_bit = str(int(c) ^ int(k))
        decrypted.append(decrypted_bit)
    return ''.join(decrypted)


plaintext = input("Введите бинарные данные (0 и 1) для шифрования: ")

if not all(bit in '01' for bit in plaintext):
    print("Неправильный формат данных. Пожалуйста, используйте только 0 и 1.")
    #TODO: преобразование в бинарный
    exit()

key = generate_one_time_pad_binary(len(plaintext))

ciphertext = one_time_pad_binary_encrypt(plaintext, key)
decrypted_text = one_time_pad_binary_decrypt(ciphertext, key)

print("\nЗашифрованные бинарные данные:")
print(ciphertext)
print("\nДешифрованные бинарные данные:")
print(decrypted_text)

