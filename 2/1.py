def xor_encrypt(plaintext, key):
    encrypted = []
    for i in range(len(plaintext)):
        encrypted_byte = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encrypted.append(encrypted_byte)
    return bytes(encrypted)

def xor_decrypt(ciphertext, key):
    decrypted = []
    for i in range(len(ciphertext)):
        decrypted_byte = ciphertext[i] ^ ord(key[i % len(key)])
        decrypted.append(decrypted_byte)
    return bytes(decrypted)

def main():
    plaintext = input("Введите текст для шифрования: ")
    key = input("Введите ключ (строка с произвольными символами): ")

    ciphertext = xor_encrypt(plaintext, key)
    decrypted_text = xor_decrypt(ciphertext, key)

    print("\nЗашифрованный текст (в байтах):")
    print(ciphertext)
    print("\nДешифрованный текст:")
    print(decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()
