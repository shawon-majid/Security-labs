
import os
import time

# print(sys.argv)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as padding_asym
from  cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey



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
        return initialization_vector+ciphertext


def aes_decrypt(data, key, mode):
    if mode == "ECB":
        decryptor = Cipher(algorithms.AES(key), modes.ECB()).decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = decryptor.update(data) + decryptor.finalize()
        plain_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return plain_data
    
    elif mode == "CFB": 
        initialization_vector = data[:16]
        decryptor = Cipher(algorithms.AES(key), modes.CFB(initialization_vector)).decryptor()
        decrypted_data = decryptor.update(data[16:]) + decryptor.finalize()
        return decrypted_data


# key = generate_key(16, 'key16.key')

# encoded = aes_encrypt(b'Hello Shawon!', key, 'ECB')
# print(encoded)
# decoded = aes_decrypt(encoded, key, 'ECB')
# print(decoded)


def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    with open('private_key.pem', 'wb') as f:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(b'password')
        )
        f.write(pem)

        
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
            password=b'password'
        )
    return private_key

def load_public_key(filename):
    with open(filename, 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read()
        )

    return public_key

def rsa_encrypt(data, public_key : RSAPublicKey):
    ciphertext = public_key.encrypt(
        data, 
        padding_asym.OAEP(
            mgf= padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def rsa_decrypt(ciphertext, private_key:RSAPrivateKey):
    plain_text = private_key.decrypt(
        ciphertext, 
        padding_asym.OAEP(
            mgf= padding_asym.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plain_text


# generate_rsa_key_pair()
# ciphertext = rsa_encrypt(b'We will launch re:elify in August 2024', load_public_key('public_key.pem'))
# print(ciphertext)
# plaintext = rsa_decrypt(ciphertext, load_private_key('private_key.pem'))
# print(plaintext)


def rsa_sign(file_name, private_key: RSAPrivateKey):
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


def rsa_verify(file_name, public_key: RSAPublicKey):
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


# rsa_sign('input.txt', load_private_key('private_key.pem'))  
# rsa_verify('input.txt', load_public_key('public_key.pem'))


def sha256_hash(file_name):
    digest = hashes.Hash(hashes.SHA256())   
    
    with open(file_name, 'rb') as f:
        data = f.read()
        digest.update(data)
        hash = digest.finalize()
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

