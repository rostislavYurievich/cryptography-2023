from itertools import cycle

def xor_encrypt(message, key):
    encrypted = []
    for c,k in zip(message, cycle(key)):
        encrypted_byte = ord(c) ^ ord(k)
        encrypted.append(encrypted_byte)
    return bytes(encrypted)

def xor_decrypt(message, key):
    decrypted = []
    for c,k in zip(message, cycle(key)):
        decrypted_byte = c ^ ord(k)
        decrypted.append(decrypted_byte)
    return bytes(decrypted)


plaintext = input("Введите текст для шифрования: ")
key = input("Введите ключ (строка с произвольными символами): ")

ciphertext = xor_encrypt(plaintext, key)
decrypted_text = xor_decrypt(ciphertext, key)

print("\nЗашифрованный текст (в байтах):\n",ciphertext)
print("\nДешифрованный текст:\n", decrypted_text.decode('utf-8'))
