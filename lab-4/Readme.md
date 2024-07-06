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

- To encrypt a file using AES with a 128-bit key in ECB mode:
  ```sh
  python test.py aes encrypt 128 ECB input.txt output.enc
  ```
- To decrypt a file encrypted with AES:
  ```sh
  python test.py aes decrypt 128 ECB output.enc input.txt
  ```
- To encrypt a file using RSA:
  ```sh
  python test.py rsa encrypt 2048 input.txt output.enc
  ```
- To decrypt a file encrypted with RSA:
  ```sh
  python test.py rsa decrypt 2048 output.enc input.txt
  ```

This script provides a flexible command-line interface for performing AES and RSA operations while measuring and displaying the execution time for each operation, allowing for performance analysis across different key sizes.
