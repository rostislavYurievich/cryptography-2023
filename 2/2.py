from itertools import cycle

def one_time_pad_encrypt(message, key):
    encrypted = []
    for c,k in zip(message,cycle(key)):
<<<<<<< HEAD
        encrypted_byte = c + k % 26
=======
        encrypted_byte = c ^ k
>>>>>>> branch_1
        encrypted.append(encrypted_byte)
    return bytes(encrypted)

def one_time_pad_decrypt(message, key):
    decrypted = []
    for c,k in zip(message,cycle(key)):
        decrypted_byte = c ^ k
        decrypted.append(decrypted_byte)
    return bytes(decrypted)

plaintext = input("Введите текст на русском для шифрования: ")

key = input("Введите ключ (строка с произвольными символами): ")

ciphertext = one_time_pad_encrypt(plaintext.encode('utf-8'), key.encode('utf-8'))
decrypted_text = one_time_pad_decrypt(ciphertext, key.encode('utf-8'))

print("\nЗашифрованный текст (в байтах):\n", ciphertext)
<<<<<<< HEAD
print("\nДешифрованный текст на русском:\n", decrypted_text.decode('utf-8'))
=======
print("\nДешифрованный текст на русском:\n", decrypted_text.decode())
>>>>>>> branch_1
