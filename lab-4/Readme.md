# Programming Symmetric & Asymmetric Crypto

Let's create program in python for the following functions:

1. AES encryption/decryption with two key lengths, 128 and 256 bits, and two modes ECB and CFB (5 marks).

## Instruction to run the code

1. Run the following command to install the requrements

```bash
pip install -r requirements.txt
```

2. Now run the following commands:

### Usage:

Here are the commands to test all the functions in `task.py` file along with the necessary commands to create additional files if needed.

1. **Generate AES Key:**

   ```sh
   python task.py generate_key 16 keys.key
   ```

2. **Encrypt Data Using AES (ECB Mode):**

   ```sh
   python task.py aes_encrypt "Hello Shawon" keys.key ECB
   ```

3. **Decrypt Data Using AES (ECB Mode):**

   ```sh
   # Replace <encrypted_data> with the output from the previous command
   python task.py aes_decrypt <encrypted_data> keys.key ECB
   ```

4. **Encrypt Data Using AES (CFB Mode):**

   ```sh
   python task.py aes_encrypt "Hello Shawon" keys.key CFB
   ```

5. **Decrypt Data Using AES (CFB Mode):**

   ```sh
   # Replace <encrypted_data> with the output from the previous command
   python task.py aes_decrypt <encrypted_data> keys.key CFB
   ```

6. **Generate RSA Key Pair:**

   ```sh
   python task.py generate_rsa_key_pair
   ```

7. **Encrypt Data Using RSA:**

   ```sh
   python task.py rsa_encrypt "Starting Date of WW3" public_key.pem
   ```

8. **Decrypt Data Using RSA:**

   ```sh
   # Replace <encrypted_data> with the output from the previous command
   python task.py rsa_decrypt <encrypted_data> private_key.pem
   ```

9. **Create a File for RSA Sign/Verify and SHA256 Hash:**

   ```sh
   echo "This is a test file." > testfile.txt
   ```

10. **Sign a File Using RSA:**

    ```sh
    python task.py rsa_sign testfile.txt private_key.pem
    ```

11. **Verify the Signature of a File Using RSA:**

    ```sh
    python task.py rsa_verify testfile.txt public_key.pem
    ```

12. **Generate SHA256 Hash of a File:**
    ```sh
    python task.py sha256_hash testfile.txt
    ```

Make sure to replace placeholders like `<encrypted_data>` with the actual encrypted data you get from the previous commands. This sequence of commands will test all the functions implemented in your `task.py` file.

## Time measurements & Observations in Graph

I used 5 different key sizes for both RSA & AES encryption and decryption. The key sizes are 16, 32, 64, 128 and 256 bytes. I measured the time taken for encryption and decryption for each key size. The following graph shows the time measurements for encryption and decryption for each key size.

To get the graph run the following command:

```bash
python time_measurement.py
```

## Acknowledgement

- [Cryptography in Python](https://cryptography.io/en/latest/)
