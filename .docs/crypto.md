---
title: CRYPTO
hide:
    - navigation
---

#

## Encrypt/Decrypt

For encrypting and decrypting the data by symmetric algorithm you can use an object
```skyant.tools.crypto.AES```.

Instance of this class contains a password. Password should provided to instance through initialisation
or will be reade from SECURITY_KEY environment variable if argument is empty.

```py linenums='1' title='encrypt then decrypt'
from skyant.tools.crypto import AES

aes = AES('password')  # or aes = AES() for read environment variable SECURITY_KEY

source = '1234'

encrypted = aes.encrypt(source)
decrypted = aes.decrypt(encrypted)

source == decrypted  # True
```

Encrypted data will be a string of bytes encoded to base64.
