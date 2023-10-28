def one_time_pad_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Длины текста и ключа должны совпадать.")

    encrypted = []
    for i in range(len(plaintext)):
        encrypted_byte = plaintext[i] + key[i] % 26
        encrypted.append(encrypted_byte)
    return bytes(encrypted)


def one_time_pad_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Длины шифротекста и ключа должны совпадать.")

    decrypted = []
    for i in range(len(ciphertext)):
        decrypted_byte = ciphertext[i] ^ key[i]
        decrypted.append(decrypted_byte)
    return bytes(decrypted)


def main():
    plaintext = input("Введите текст на русском для шифрования: ")
    plaintext_bytes = plaintext.encode('utf-8')

    key = input("Введите ключ (строка с произвольными символами): ")
    key_bytes = key.encode('utf-8')

    if len(plaintext_bytes) != len(key_bytes):
        print("Длины текста и ключа не совпадают.")
        return

    ciphertext = one_time_pad_encrypt(plaintext_bytes, key_bytes)
    decrypted_text = one_time_pad_decrypt(ciphertext, key_bytes)

    print("\nЗашифрованный текст (в байтах):")
    print(ciphertext)
    print("\nДешифрованный текст на русском:")
    print(decrypted_text.decode('utf-8'))


if __name__ == "__main__":
    main()
