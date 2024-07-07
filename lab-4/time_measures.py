import matplotlib.pyplot as plt

# The data I used to plot the graphs is just a placeholder. Replace it with the actual data you collected.
key_sizes = [16, 32, 64, 128, 256]  # Key sizes in bits
aes_encryption_times_ecb = [0.001, 0.002, 0.003, 0.005, 0.009]  
aes_decryption_times_ecb = [0.0015, 0.003, 0.004, 0.006, 0.01]  
aes_encryption_times_cfb = [0.002, 0.0035, 0.005, 0.008, 0.012]  
aes_decryption_times_cfb = [0.0025, 0.004, 0.006, 0.009, 0.013]  
rsa_key_sizes = [2048, 3072, 4096]  
rsa_key_generation_times = [0.5, 0.8, 1.2]  
rsa_public_key_load_times = [0.001, 0.002, 0.003]  
rsa_private_key_load_times = [0.0012, 0.0025, 0.0038]  
rsa_encryption_times = [0.003, 0.006, 0.01]  
rsa_decryption_times = [0.004, 0.007, 0.012]  

# Plot AES execution times
plt.figure(figsize=(12, 6))

# AES ECB mode
plt.subplot(1, 2, 1)
plt.plot(key_sizes, aes_encryption_times_ecb, marker='o', label='AES ECB Encryption')
plt.plot(key_sizes, aes_decryption_times_ecb, marker='s', label='AES ECB Decryption')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('AES ECB Encryption and Decryption Times')
plt.legend()
plt.grid(True)

# AES CFB mode
plt.subplot(1, 2, 2)
plt.plot(key_sizes, aes_encryption_times_cfb, marker='o', label='AES CFB Encryption')
plt.plot(key_sizes, aes_decryption_times_cfb, marker='s', label='AES CFB Decryption')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('AES CFB Encryption and Decryption Times')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Plot RSA execution times
plt.figure(figsize=(12, 6))

# RSA Key Generation
plt.subplot(2, 2, 1)
plt.plot(rsa_key_sizes, rsa_key_generation_times, marker='o', label='RSA Key Generation')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('RSA Key Generation Time')
plt.legend()
plt.grid(True)

# RSA Key Load (Public Key)
plt.subplot(2, 2, 2)
plt.plot(rsa_key_sizes[:len(rsa_public_key_load_times)], rsa_public_key_load_times, marker='o', label='RSA Public Key Load')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('RSA Public Key Load Time')
plt.legend()
plt.grid(True)

# RSA Key Load (Private Key)
plt.subplot(2, 2, 3)
plt.plot(rsa_key_sizes[:len(rsa_private_key_load_times)], rsa_private_key_load_times, marker='o', label='RSA Private Key Load')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('RSA Private Key Load Time')
plt.legend()
plt.grid(True)

# RSA Encryption and Decryption
plt.subplot(2, 2, 4)
plt.plot(rsa_key_sizes[:len(rsa_encryption_times)], rsa_encryption_times, marker='o', label='RSA Encryption')
plt.plot(rsa_key_sizes[:len(rsa_decryption_times)], rsa_decryption_times, marker='s', label='RSA Decryption')
plt.xlabel('Key Size (bits)')
plt.ylabel('Time (seconds)')
plt.title('RSA Encryption and Decryption Times')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
