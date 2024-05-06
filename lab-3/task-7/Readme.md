## Task 7

The instructions are followed in the given steps:

1. Create a text file and add some text in it.
2. Generate the hash value H1 for this file using `SHA-256` hash algorithm using the following command:

```bash
openssl dgst -sha256 -hmac "abc123" plain.txt
```

Generated hash:

```
HMAC-SHA2-256(plain.txt)= 6b3e344f18f4e48a9d00664950c6e45a370a360420168407914fa398879f6d86
```

3. Change one bit of the input file. Open the file using `ghex` and change any of the bit.
4. Again generate the hash value H2

```bash
openssl dgst -sha256 -hmac "abc123" plain.txt
```

Generated hash:

```
HMAC-SHA2-256(plain.txt)= 268ade015562feca33caea7fce07b95712525acd4cd6003246ec1d7e92deb9ef
```

We can see that the hash values (H1 and H2) are not same. The we can use the following code to see how many bits are same.

```cpp
int main(){
    string h1, h2;
    cin >> h1 >> h2;
    int same = 0;
    for(int i = 0; i < h1.size(); i++){
        if(h1[i] == h2[i]){
            same++;
        }
    }
    cout << "Number of same bit: " << same << "\n";
    return 0;
}
```

Output:

```
Number of same bit: 3
```

So we can see that chaning only 1 bit has totally changed the hash value.

Now lets try the same thing with `Message Digest 5` Algorithm.

Everything will be similer but this time the command will be

```bash
openssl dgst -md5 -hmac "abc123" plain.txt
```

**H1**

```
HMAC-MD5(plain.txt)= c0acb07a15c5fb7633f5294363295b28
```

**H2**

```
HMAC-MD5(plain.txt)= 8e0175ac62d72382fe3014fd5e67855c
```

Again run the main.cpp with the given hash values.

```
Number of same bit: 0
```

We can see that there is no same bit in the generated hash. That means that chaning only one bit in the input file entirely changes the hash value.
