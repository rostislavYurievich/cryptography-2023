import random


def generate_one_time_pad_binary(length):
    return ''.join([str(random.randint(0, 1)) for _ in range(length)])


def one_time_pad_binary_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Длины текста и ключа должны совпадать.")

    encrypted = []
    for i in range(len(plaintext)):
        encrypted_bit = str(int(plaintext[i]) ^ int(key[i]))
        encrypted.append(encrypted_bit)
    return ''.join(encrypted)


def one_time_pad_binary_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Длины шифротекста и ключа должны совпадать.")

    decrypted = []
    for i in range(len(ciphertext)):
        decrypted_bit = str(int(ciphertext[i]) ^ int(key[i]))
        decrypted.append(decrypted_bit)
    return ''.join(decrypted)


def main():
    plaintext = input("Введите бинарные данные (0 и 1) для шифрования: ")

    if not all(bit in '01' for bit in plaintext):
        print("Неправильный формат данных. Пожалуйста, используйте только 0 и 1.")
        return

    key = generate_one_time_pad_binary(len(plaintext))

    ciphertext = one_time_pad_binary_encrypt(plaintext, key)
    decrypted_text = one_time_pad_binary_decrypt(ciphertext, key)

    print("\nЗашифрованные бинарные данные:")
    print(ciphertext)
    print("\nДешифрованные бинарные данные:")
    print(decrypted_text)


if __name__ == "__main__":
    main()
