## Task 2

**AES ECB Encryption**

1. Download a .bmp file from internet & rename it sample.bmp
2. Encrypt the picture with (ECB) mode with the following command:

```bash
openssl enc -aes-128-ecb -e  -in sample.bmp -out encrypted-ecb.bmp -K 00112233445566778889aabbccd3322a
```

3. Now open the original picture with `ghex`:

```bash
ghex sample.bmp
```

4. Copy the first 54 bytes. (header information)
5. Now open the encrypted image with `ghex`:

```bash
ghex encrypted-ecb.bmp
```

6. Replace the first 54 bytes with the original header information
7. Now open the `encrypted-ecb.bmp` to see the encrypted image.
   We can see that the shape of the snail is understandable but the snail itself is not visible.

**AES CBC Encryption**

1. Encrypt the picture with (CBC) mode with the following command:

```bash
openssl enc -aes-128-cbc -e  -in sample.bmp -out encrypted-cbc.bmp \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

2. Now open the original picture with `ghex`:

```bash
ghex sample.bmp
```

3. Copy the first 54 bytes. (header information)
4. Now open the encrypted image with `ghex`:

```bash
ghex encrypted-cbc.bmp
```

5. Replace the first 54 bytes with the original header information
6. Now open the `encrypted-cbc.bmp` to see the encrypted image.
   Now we can see that the image is completely incomprehensible. Even the shape of the snail is not visible.

**_Analysis & Comparison between ECB & CBC Mode_**

CBC (Cipher Block Chaining) and ECB (Electronic Codebook) are two modes of operation in block cipher encryption:

1. **ECB Mode (Electronic Codebook)**:

   - In ECB mode, each block of plaintext is encrypted independently with the same key.
   - It lacks diffusion, meaning identical blocks of plaintext will result in identical blocks of ciphertext.
   - This can lead to security vulnerabilities, especially in image encryption, where patterns might be preserved.

2. **CBC Mode (Cipher Block Chaining)**:
   - In CBC mode, each plaintext block is XORed with the previous ciphertext block before encryption.
   - This adds diffusion, making it more resistant to patterns and repetition in the plaintext.
   - CBC mode requires an Initialization Vector (IV) for the first block to start the chaining process.

**Comparison**:

- ECB is simpler and faster, but less secure, especially for images.
- CBC is more secure due to its chaining mechanism, but slightly slower and requires an IV.

For image encryption, CBC is generally preferred over ECB due to its better resistance to pattern preservation and higher security.
