
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import (load_pem_private_key, load_pem_public_key)
from cryptography.exceptions import InvalidSignature

def generate_ec_key_pair():
    return ec.generate_private_key(
        ec.SECP256R1(),
        default_backend()
    )

def get_public_key(private_key):
    return private_key.public_key()

def create_signature(private_key, message):
    return private_key.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )

def verify_signature(public_key, signature, message):
    try:
        public_key.verify(
            signature,
            message,
            ec.ECDSA(hashes.SHA256())
        )
        return "Подпись верифицирована: True"
    except InvalidSignature:
        return "Подпись верифицирована: False"

def main():
    private_key = generate_ec_key_pair()
    public_key = get_public_key(private_key)

    message = input("Введите сообщение для подписи: ").encode()

    signature = create_signature(private_key, message)

    result = verify_signature(public_key, signature, message)
    print(result)

    print("\nИнформация о ключах:")
    print("Открытый ключ:")
    print(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode())
    print("\nЗакрытый ключ:")
    print(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ).decode())

if __name__ == "__main__":
    main()
