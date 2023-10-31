from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization


def generate_rsa_key_pair():
    """Генерация закрытого ключа"""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

def get_public_key(private_key):
    """Генерация открытого ключа"""
    return private_key.public_key()

def get_private_key_info(private_key):
    """Информация для вывода"""
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()  # Без пароля
    ).decode()

def create_signature(private_key, message):
    """Подпись сообщения"""
    return private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(public_key, signature, message):
    """Проверка подписи"""
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return "Проверка подписи прошла успешно"
    except InvalidSignature:
        return "Проверка подписи не удалась"

# Генерация ключевой пары
private_key = generate_rsa_key_pair()
public_key = get_public_key(private_key)

# Ввод сообщения от пользователя
message = input("Введите сообщение для подписи: ").encode()

# Создание подписи
signature = create_signature(private_key, message)

# Проверка подписи
result = verify_signature(public_key, signature, message)
print(result)

# Вывод информации о ключах
print("\nИнформация о ключах:\n", get_private_key_info(private_key))
print("Открытый ключ:\n",
    public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode())
print("\nЗакрытый ключ:\n", get_private_key_info(private_key))
