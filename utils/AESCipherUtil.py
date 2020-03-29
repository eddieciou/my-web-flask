# coding=utf-8
import base64

from Crypto import Random
from Crypto.Cipher import AES

BASE = 16


def pad(s):
    return s + (BASE - len(s) % BASE) * chr(BASE - len(s) % BASE)


def un_pad(s):
    return s[0:-ord(s[-1])]


class AESCipherUtil:

    def __init__(self, key):
        self.key = key.encode("utf-8")

    def encrypt(self, raw):
        raw = pad(raw.decode()).encode("utf-8")
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return un_pad(cipher.decrypt(enc[16:]).decode("utf-8"))
