from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
from pathlib import Path

def load_private_key(path):
    return serialization.load_pem_private_key(Path(path).read_bytes(), password=None)

def load_public_key(path):
    return serialization.load_pem_public_key(Path(path).read_bytes())

def sign_message(private_key, message: bytes) -> bytes:
    return private_key.sign(
        message,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

def verify_signature(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False