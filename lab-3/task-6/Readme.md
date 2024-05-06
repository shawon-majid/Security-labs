## Task 6

The instructions are followed in the given steps:

1. Create a text file and add some text.
2. Generate a keyed hash using `HMAC-MD5` algorithm

```bash
openssl dgst -md5 -hmac "abcdefg" plain.txt
```

Generated Hash:

```
HMAC-MD5(plain.txt)= 9d6922d9ac143565588dbcfe4d606251
```

3. Generate a keyed hash using `HMAC-SHA256` algorithm

```bash
openssl dgst -sha256 -hmac "abc123" plain.txt
```

Generated Hash:

```
HMAC-SHA2-256(plain.txt)= fc1d05cc956ecd59432062ee2dab4b150fcbc4650562bd6f264a1e834fa2ae63
```

4. Generate a keyed hash using `HMAC-SHA1` algorithm

```bash
openssl dgst -sha1 -hmac "abc123efg" plain.txt
```

Generated Hash:

```
HMAC-SHA1(plain.txt)= 0abe0439a58f1dd29ad569d6191386f67a72416f
```

Regarding the key size in HMAC:

1. **Fixed Size:** No, HMAC does not require a key with a fixed size. It can accept keys of any length.
2. **Key Size:** The key size should ideally be chosen based on the security requirements of the application and the cryptographic algorithm being used. However, for HMAC, it's recommended to use keys that are at least as long as the block size of the underlying hash function. For example:

- For HMAC-MD5: Recommended minimum key size is 128 bits (16 bytes).
- For HMAC-SHA1: Recommended minimum key size is 160 bits (20 bytes).
- For HMAC-SHA256: Recommended minimum key size is 256 bits (32 bytes).

Using longer keys can provide better security against brute-force attacks, but excessively long keys may not necessarily enhance security significantly and can incur additional overhead in terms of processing and storage.
