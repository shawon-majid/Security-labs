## Task 3

The goal of this task to understand the properties of various encryption modes.

1. Create a text file that is atleast 64 bytes long.
2. Encrypt the file using AES-128 Cipher using the following command

```bash
openssl enc -aes-128-ecb -e  -in plain.txt -out encrypted-ecb.bin -K 00112233445566778889aabbccd3322a
```

3. Now corrupt a single bit of the 30th byte in the encrypted file.
   - Open the file using ghex
   - Change the first bit of 30th byte
4. Now decrypt the file using the following command.

```bash
openssl enc -aes-128-ecb -d  -in encrypted-ecb.bin -out decrypted-ecb.txt -K 00112233445566778889aabbccd3322a
```

Now let's do it with the other modes:

1. Using `CBC mode`:
   **Encrypt:**

```bash
openssl enc -aes-128-cbc -e  -in plain.txt -out encrypted-cbc.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

**Corrupt the file**
**Decrypt:**

```bash
openssl enc -aes-128-cbc -d  -in encrypted-cbc.bin -out decrypted-cbc.txt \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

2. Using `CFB mode`:
   **Encrypt:**

```bash
openssl enc -aes-128-cfb -e  -in plain.txt -out encrypted-cfb.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

**Corrupt the file**
**Decrypt:**

```bash
openssl enc -aes-128-cfb -d  -in encrypted-cfb.bin -out decrypted-cfb.txt \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

3. Using `OFB mode`:
   **Encrypt:**

```bash
openssl enc -aes-128-ofb -e  -in plain.txt -out encrypted-ofb.bin \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

**Corrupt the file**
**Decrypt:**

```bash
openssl enc -aes-128-ofb -d  -in encrypted-ofb.bin -out decrypted-ofb.txt \
                 -K  00112233445566778889aabbccddeeff \
                 -iv 01020304050607083241231213124f23
```

**Results**
|Original File|Corrupted File| Mode |
|-----------|----------------|------|
|Its raining in sylhet. The atmosphere is awesome, I am remembering the day of return from Dhaka in 2017| Its raining in s?d??1????9N:<?phere is awesome, I am remembering the day of return from Dhaka in 2017| ECB |
|Its raining in sylhet. The atmosphere is awesome, I am remembering the day of return from Dhaka in 2017| Its raining in sR�l��Ju�����mphere is awesoe, I am remembering the day of return from Dhaka in 2017| CBC |
|Its raining in sylhet. The atmosphere is awesome, I am remembering the day of return from Dhaka in 2017| Its raining in sylhet. The atm�s�_�T��Y�1�x$, I am remembering the day of return from Dhaka in 2017| CFB |
|Its raining in sylhet. The atmosphere is awesome, I am remembering the day of return from Dhaka in 2017|Its raining in sylhet. The atm�sphere is awesome, I am remembering the day of return from Dhaka in 2017| OFB |

### Analysis

Based on the provided results, let's analyze the information recovery for each encryption mode:

1. **ECB Mode**:

   - Recoverable Information: "Its raining in s" (16 bytes)
   - Explanation: In ECB mode, each block is encrypted independently. Therefore, the corruption only affects the specific block where it occurred. The rest of the plaintext remains intact.

2. **CBC Mode**:

   - Recoverable Information: "Its raining in s" (16 bytes)
   - Explanation: While CBC mode encrypts blocks in a chained manner, the corruption in one block affects the decryption of subsequent blocks. However, the first block can still be recovered as it only depends on the IV and the first block of ciphertext.

3. **CFB Mode**:

   - Recoverable Information: "Its raining in sylhet. The atm" (32 bytes)
   - Explanation: In CFB mode, the corruption in one ciphertext block affects the decryption of subsequent blocks. However, due to the feedback mechanism, only a part of the subsequent blocks is corrupted. As a result, more information can be recovered compared to CBC mode.

4. **OFB Mode**:
   - Recoverable Information: "Its raining in sylhet. The atm" (32 bytes)
   - Explanation: Similar to CFB mode, the corruption in one ciphertext block affects the decryption of subsequent blocks. However, in OFB mode, the feedback mechanism is independent of the plaintext, resulting in a similar recovery as in CFB mode.

**Implications**:

- ECB mode offers the least security and diffusion, as evident from the limited recoverable information.
- CBC mode provides better security compared to ECB but still suffers from partial corruption propagation.
- CFB and OFB modes offer improved diffusion, allowing for more recoverable information compared to CBC mode, although they are still susceptible to partial corruption propagation.
