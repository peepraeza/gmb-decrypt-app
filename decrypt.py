import sys

from Crypto.Cipher import AES
from Crypto.Random import new as Random
from hashlib import sha256
from base64 import b64encode, b64decode


class AESCipher:
    def __init__(self, data, gmbKey):
        self.block_size = 16
        self.data = data
        self.key = sha256(gmbKey.encode()).digest()[:16]
        self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * \
                             chr(self.block_size - len(s) % self.block_size)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def encrypt(self):
        # try:
        print('call function encrypt with plain message: ', self.data, file=sys.stderr)
        plain_text = self.pad(self.data)
        iv = Random().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        print('before encrypt', file=sys.stderr)
        enc = b64encode(iv + cipher.encrypt(plain_text.encode())).decode()
        return enc
        # except:
        #     return 'error, can not encrypt with these data.'

    def decrypt(self):
        try:
            print('call function decrypt with encrypt message: ', self.data, file=sys.stderr)
            cipher_text = b64decode(self.data.encode())
            iv = cipher_text[:self.block_size]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            print('before decrypt', file=sys.stderr)
            dec = self.unpad(cipher.decrypt(cipher_text[self.block_size:])).decode()
            print('return decrypt message: ', dec, file=sys.stderr)
            return dec
        except:
            return 'error, can not decrypt with these data.'
