import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding as padding_asym
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey


def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Save private key to a file
    with open('private_key.pem', 'wb') as f:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()  # No encryption for private key
        )
        f.write(pem)

    # Extract public key from private key and save to a file
    public_key = private_key.public_key()
    with open('public_key.pem', 'wb') as f:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        f.write(pem)


def load_private_key(file_name):
    with open(file_name, 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,  # No password for loading private key
        )
    return private_key


def load_public_key(filename):
    with open(filename, 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )
    return public_key


def rsa_encrypt(data, public_key: RSAPublicKey):
    ciphertext = public_key.encrypt(
        data.encode(),  # Convert data to bytes before encryption
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext.hex()


def rsa_decrypt(ciphertext, private_key: RSAPrivateKey):
    ciphertext_bytes = bytes.fromhex(ciphertext)  # Convert hexadecimal string to bytes
    plaintext = private_key.decrypt(
        ciphertext_bytes,
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()  # Decode decrypted bytes to string


# # Generate RSA key pair (run once to generate keys)
# generate_rsa_key_pair()

# # Example usage
# plaintext = 'We will launch re:elify in August 2024'

# # Encrypt and decrypt using RSA
# ciphertext = rsa_encrypt(plaintext, load_public_key('public_key.pem'))
# print("Encrypted:", ciphertext)

# decrypted_text = rsa_decrypt(ciphertext, load_private_key('private_key.pem'))
# print("Decrypted:", decrypted_text)
