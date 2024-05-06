## Task 5

The instructions are followed by the given steps:

1. Create a text file with some text in it.
2. Use the `SHA-256` (Secure Hash Algorithm) hashing algorithm by the following command:

```bash
openssl dgst -sha256 sample.txt
```

Generated hash:

```
SHA2-256(sample.txt)= 19c35534df2643f9df4d0ca479bd0800903dc8f0207af562e659c513ac68ada1
```

3. Use the `Message digest 5` hashing algorithm by the following command:

```bash
openssl dgst -md5 sample.txt
```

Generated hash:

```
MD5(sample.txt)= 66ec600013182b19c6507c6b727d7628
```

4. Use the `SHA-1` hashing algorithm by the following command:

```bash
openssl dgst -sha1 sample.txt
```

Generated hash:

```
SHA1(sample.txt)= 08fee9c47c082aeb6b29136882f9ceac502e0083
```

### Observations

Observations on the three hashing algorithms:

1. **SHA-256**:

- SHA-256 produces a 256-bit (32-byte) hash value.
- It is widely used for cryptographic applications and digital signatures.
- The hash value is longer compared to MD5 and SHA-1, providing better security against collisions.

2. **MD5**:

- MD5 produces a 128-bit (16-byte) hash value.
- It is fast and commonly used for checksums and data integrity verification.
- However, MD5 is considered broken and vulnerable to collision attacks, so it's not recommended for security-sensitive applications.

3. **SHA-1**:

- SHA-1 produces a 160-bit (20-byte) hash value.
- It was widely used but is now considered weak and vulnerable to collision attacks.
- Despite its vulnerabilities, it's still used in legacy systems and applications.

**Comparison**

- SHA-256 provides the longest hash value and is the most secure among the three.
- MD5, while fast, is considered insecure and should be avoided for security purposes.
- SHA-1 is stronger than MD5 but is also vulnerable to collision attacks, making it less secure than SHA-256. It's being phased out in favor of more secure hashing algorithms.
