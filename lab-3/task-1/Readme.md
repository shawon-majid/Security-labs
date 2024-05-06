## Task 1

1. Create a text file with some text
2. Now we can encrypt this text file the following command using `AES-128-CBC`:

```bash
openssl enc -aes-128-cbc -e  -in plain.txt -out cipher-aes-128-cbc.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

3. We can also decrypt the same file with the following command:

```bash
openssl enc -aes-128-cbc -d  -in cipher-aes-128-cbc.bin \
                            -out   decrypted-aes-128-cbc.txt \
                            -K  00112233445566778889aabbccddeeff \
                            -iv 01020304050607083241231213124f23
```

4. We can also Encrypt & Decrypt the file using two other modes:

   1. `AES-128-ECB`:
      Encryption:

   ```bash
   openssl enc -aes-128-ecb -e  -in plain.txt -out cipher-aes-128-ecb.bin -K 00112233445566778889aabbccd3322a
   ```

   Decryption:

   ```bash
   openssl enc -aes-128-ecb -d  -in cipher-aes-128-ecb.bin -out decrypted-aes-128-ecb.txt -K  00112233445566778889aabbccd3322a
   ```

   2. `AES-128-CFB`:
      Encryption:

   ```bash
   openssl enc -aes-128-cfb -e  -in plain.txt \
               -out cipher-aes-128-cfb.bin \
               -K  00112233445566778889aabbccddeeff \
               -iv 01020304050607083241231213124f23
   ```

   Decryption:

   ```bash
   openssl enc -aes-128-cfb -d  -in cipher-aes-128-cfb.bin \
               -out decrypted-aes-128-cfb.txt \
               -K  00112233445566778889aabbccddeeff \
               -iv 01020304050607083241231213124f23
   ```
