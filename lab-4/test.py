import os
import sys
import time
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as padding_asym
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey

KEY_DIR = 'keys'

def generate_key(key_size, file_name):
    key = os.urandom(key_size)
    with open(file_name, 'wb') as f:
        f.write(key)
    return key

def read_key(file_name):
    with open(file_name, 'rb') as f:
        key = f.read()
    return key

def aes_encrypt(data, key, mode):
    if mode == 'ECB':
        encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext
    elif mode == 'CFB':
        initialization_vector = os.urandom(16)
        encryptor = Cipher(algorithms.AES(key), modes.CFB(initialization_vector)).encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        return initialization_vector + ciphertext

def aes_decrypt(data, key, mode):
    if mode == 'ECB':
        decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = decryptor.update(data) + decryptor.finalize()
        plain_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return plain_data
    elif mode == 'CFB':
        initialization_vector = data[:16]
        decryptor = Cipher(algorithms.AES(key), modes.CFB(initialization_vector)).decryptor()
        decrypted_data = decryptor.update(data[16:]) + decryptor.finalize()
        return decrypted_data

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    with open(os.path.join(KEY_DIR, 'private_key.pem'), 'wb') as f:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'password')
        )
        f.write(pem)
    public_key = private_key.public_key()
    with open(os.path.join(KEY_DIR, 'public_key.pem'), 'wb') as f:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        f.write(pem)

def load_private_key(file_name):
    with open(file_name, 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=b'password'
        )
    return private_key

def load_public_key(file_name):
    with open(file_name, 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )
    return public_key

def rsa_encrypt(data, public_key: RSAPublicKey):
    ciphertext = public_key.encrypt(
        data,
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(ciphertext, private_key: RSAPrivateKey):
    plain_text = private_key.decrypt(
        ciphertext,
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plain_text

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def main():
    if not os.path.exists(KEY_DIR):
        os.makedirs(KEY_DIR)

    parser = argparse.ArgumentParser(description='AES and RSA Encryption/Decryption with Timing')
    parser.add_argument('algorithm', choices=['aes', 'rsa'], help='Select algorithm to use (aes or rsa)')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Select action to perform (encrypt or decrypt)')
    parser.add_argument('key_size', type=int, help='Key size in bits (e.g., 128, 256)')
    parser.add_argument('mode', choices=['ECB', 'CFB'], help='AES mode of operation (ECB or CFB)')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')

    args = parser.parse_args()

    if args.algorithm == 'aes':
        key_file = os.path.join(KEY_DIR, f'aes_key_{args.key_size}.key')
        if args.action == 'encrypt':
            key = generate_key(args.key_size // 8, key_file)
            with open(args.input_file, 'rb') as f:
                data = f.read()
            _, elapsed_time = measure_time(aes_encrypt, data, key, args.mode)
            with open(args.output_file, 'wb') as f:
                f.write(_)
            print(f'Encryption completed in {elapsed_time} seconds.')
        elif args.action == 'decrypt':
            key = read_key(key_file)
            with open(args.input_file, 'rb') as f:
                data = f.read()
            _, elapsed_time = measure_time(aes_decrypt, data, key, args.mode)
            with open(args.output_file, 'wb') as f:
                f.write(_)
            print(f'Decryption completed in {elapsed_time} seconds.')

    elif args.algorithm == 'rsa':
        if args.action == 'encrypt':
            generate_rsa_key_pair()
            public_key_file = os.path.join(KEY_DIR, 'public_key.pem')
            public_key = load_public_key(public_key_file)
            with open(args.input_file, 'rb') as f:
                data = f.read()
            _, elapsed_time = measure_time(rsa_encrypt, data, public_key)
            with open(args.output_file, 'wb') as f:
                f.write(_)
            print(f'Encryption completed in {elapsed_time} seconds.')
        elif args.action == 'decrypt':
            private_key_file = os.path.join(KEY_DIR, 'private_key.pem')
            private_key = load_private_key(private_key_file)
            with open(args.input_file, 'rb') as f:
                data = f.read()
            _, elapsed_time = measure_time(rsa_decrypt, data, private_key)
            with open(args.output_file, 'wb') as f:
                f.write(_)
            print(f'Decryption completed in {elapsed_time} seconds.')

if __name__ == '__main__':
    main()
