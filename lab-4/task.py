
import os
import time

# print(sys.argv)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as padding_asym
from  cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey
import argparse



def generate_key(key_size, file_name):

    start = time.time()


    key = os.urandom(key_size)  

    with open(file_name, 'wb') as f:
        f.write(key)


    end = time.time()

    elapsed_time = end - start
    print(f'Elapsed time: {elapsed_time} seconds')
    return key


def read_key(file_name):
    with open(file_name, 'rb') as f:
        key = f.read()
    return key



def aes_encrypt(data, key, mode):

    start = time.time()

    if mode == 'ECB':
        encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()


        end = time.time()

        print(f'Elapsed time: {end - start} seconds')

        return ciphertext.hex()  # Return ciphertext as a hexadecimal string

    elif mode == 'CFB':

        initialization_vector = os.urandom(16)
        encryptor = Cipher(algorithms.AES(key), modes.CFB(initialization_vector)).encryptor()
        ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

        end = time.time()

        print(f'Elapsed time: {end - start} seconds')
        return initialization_vector.hex() + ciphertext.hex()  # Return IV + ciphertext as hexadecimal string


def aes_decrypt(data, key, mode):

    start = time.time()

    if mode == "ECB":
        decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
        decrypted_data = decryptor.update(bytes.fromhex(data)) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()


        end = time.time()
        return unpadded_data.decode()


# key = generate_key(16, 'key16.key')

# encoded = aes_encrypt(b'Hello Shawon!', key, 'ECB')
# print(encoded)
# decoded = aes_decrypt(encoded, key, 'ECB')
# print(decoded)

def generate_rsa_key_pair():

    start = time.time()

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

    end = time.time()

    print(f'Elapsed time: {end - start} seconds')



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

    start = time.time()

    ciphertext = public_key.encrypt(
        data.encode(),  # Convert data to bytes before encryption
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    end = time.time()

    print(f'Elapsed time: {end - start} seconds')
    return ciphertext.hex()


def rsa_decrypt(ciphertext, private_key: RSAPrivateKey):

    start = time.time()

    ciphertext_bytes = bytes.fromhex(ciphertext)  # Convert hexadecimal string to bytes
    plaintext = private_key.decrypt(
        ciphertext_bytes,
        padding_asym.OAEP(
            mgf=padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


    end = time.time()

    print(f'Elapsed time: {end - start} seconds')
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


def rsa_sign(file_name, private_key: RSAPrivateKey):


    start = time.time()

    with open(file_name, 'rb') as f:
        data = f.read()

    signature = private_key.sign(
        data, 
        padding_asym.PSS(
            mgf= padding_asym.MGF1(hashes.SHA256()),
            salt_length=padding_asym.PSS.MAX_LENGTH
        ), 
        hashes.SHA256()
    )
    
    with open(file_name+'.sig', 'wb') as f:
        f.write(signature)

    end = time.time()

    print(f'Elapsed time: {end - start} seconds')


def rsa_verify(file_name, public_key: RSAPublicKey):

    start = time.time()

    with open(file_name, 'rb') as f:
        data = f.read()

    with open(file_name+'.sig', 'rb') as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            data,
            padding_asym.PSS(
                mgf= padding_asym.MGF1(hashes.SHA256()),
                salt_length=padding_asym.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print('Signature is valid')
    except:
        print('Signature is invalid')

    end = time.time()

    print(f'Elapsed time: {end - start} seconds')


# rsa_sign('input.txt', load_private_key('private_key.pem'))  
# rsa_verify('input.txt', load_public_key('public_key.pem'))


def sha256_hash(file_name):
    start = time.time()

    digest = hashes.Hash(hashes.SHA256())   
    
    with open(file_name, 'rb') as f:
        data = f.read()
        digest.update(data)
        hash = digest.finalize()

    end = time.time()

    print(f'Elapsed time: {end - start} seconds')
    return hash

# h1 = sha256_hash('input.txt')
# h2 = sha256_hash('input2.txt')

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    elapsed_time = end - start
    return result, elapsed_time


# _, elapsed_time = measure_time(rsa_encrypt, b'hello world', load_public_key('public_key.pem')     )



def main():
    parser = argparse.ArgumentParser(description='Encrypt and Decrypt files using AES and RSA') 
    subparsers = parser.add_subparsers(dest='command', help='sub-command help') 
     
    # Command to generate AES key
    parser_generate_key = subparsers.add_parser('generate_key')
    parser_generate_key.add_argument('key_size', type=int, help='Size of the key in bytes')
    parser_generate_key.add_argument('key_file', type=str, help='File to store the generated key') 
     
     
    # AES encryption/decryption
    parser_aes_enc = subparsers.add_parser('aes_encrypt', help='AES encryption')
    parser_aes_enc.add_argument('data', type=str, help='Data to encrypt')
    parser_aes_enc.add_argument('key_file', type=str, help='Key file')
    parser_aes_enc.add_argument('mode', choices=['ECB', 'CFB'], help='AES mode')

    parser_aes_dec = subparsers.add_parser('aes_decrypt', help='AES decryption')
    parser_aes_dec.add_argument('data', type=str, help='Data to decrypt')
    parser_aes_dec.add_argument('key_file', type=str, help='Key file')
    parser_aes_dec.add_argument('mode', choices=['ECB', 'CFB'], help='AES mode')

    parser_rsa_gen = subparsers.add_parser('generate_rsa_key_pair', help='Generate RSA key pair')   

    parser_rsa_enc = subparsers.add_parser('rsa_encrypt', help='RSA encryption')    
    parser_rsa_enc.add_argument('data', type=str, help='Data to encrypt')
    parser_rsa_enc.add_argument('key_file', type=str, help='Key file')

    parser_rsa_dec = subparsers.add_parser('rsa_decrypt', help='RSA decryption')
    parser_rsa_dec.add_argument('data', type=str, help='Data to decrypt')
    parser_rsa_dec.add_argument('key_file', type=str, help='Key file')

    parser_rsa_sign = subparsers.add_parser('rsa_sign', help='RSA sign')
    parser_rsa_sign.add_argument('file_name', type=str, help='File to sign')
    parser_rsa_sign.add_argument('key_file', type=str, help='Key file')

    parser_rsa_verify = subparsers.add_parser('rsa_verify', help='RSA verify')
    parser_rsa_verify.add_argument('file_name', type=str, help='File to verify')
    parser_rsa_verify.add_argument('key_file', type=str, help='Key file')

    parser_hash = subparsers.add_parser('sha256_hash', help='SHA256 hash')
    parser_hash.add_argument('file_name', type=str, help='File to hash')


    



    args = parser.parse_args()

    if args.command == 'generate_key':
        generate_key(args.key_size, args.key_file)
        print(f'Key of size: {args.key_size} generated and saved in {args.key_file}')

    if args.command == 'aes_encrypt':
        key = read_key(args.key_file)
        encoded = aes_encrypt(args.data, key, args.mode)
        print(encoded)

    if args.command == 'aes_decrypt':
        key = read_key(args.key_file)
        decoded = aes_decrypt(args.data, key, args.mode)
        print(decoded)


    if args.command == 'generate_rsa_key_pair':
        generate_rsa_key_pair()
        print('RSA key pair generated and saved in private_key.pem and public_key.pem')

    if args.command == 'rsa_encrypt':
        public_key = load_public_key(args.key_file)
        ciphertext = rsa_encrypt(args.data, public_key)
        print("Encrypted:", ciphertext)

    if args.command == 'rsa_decrypt':
        private_key = load_private_key(args.key_file)
        decrypted_text = rsa_decrypt(args.data, private_key)
        print("Decrypted:", decrypted_text)

    if args.command == 'rsa_sign':
        private_key = load_private_key(args.key_file)
        rsa_sign(args.file_name, private_key)
        print('Signature created and saved in', args.file_name+'.sig')

    if args.command == 'rsa_verify':
        public_key = load_public_key(args.key_file)
        rsa_verify(args.file_name, public_key)

    if args.command == 'sha256_hash':
        hash = sha256_hash(args.file_name)
        print('SHA256 hash:', hash.hex())





    





if __name__ == '__main__':
    main()