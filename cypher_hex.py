#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify

input = '80:c9:55:64:73:f0'
CRYPTO_KEY= b'8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3'
CRYPTO_IV= b'rBEssDfxofOveRxR'

BLOCK_SIZE = 16


def encrypt(data):
    aes = AES.new(CRYPTO_KEY, AES.MODE_CBC, CRYPTO_IV)
    encrypted = aes.encrypt(pad(data.encode(), BLOCK_SIZE))
    return hexlify(encrypted)


def decrypt(edata):
    edata = unhexlify(edata)
    aes = AES.new(CRYPTO_KEY, AES.MODE_CBC, CRYPTO_IV)
    return unpad(aes.decrypt(edata), BLOCK_SIZE)


def main():
    output = encrypt(input) 
    plaintext = decrypt(output)

    print(output.decode("utf-8"))
    print(plaintext.decode("utf-8"))


if __name__ == "__main__":
    main()
