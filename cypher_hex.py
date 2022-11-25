#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify

input = '80:c9:55:64:73:f0'
CRYPTO_KEY= '8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3'
CRYPTO_IV= 'rBEssDfxofOveRxR'

BLOCK_SIZE = 16


def encrypt(input):
    key = bytes(CRYPTO_KEY, 'utf-8')
    iv = bytes(CRYPTO_IV, 'utf-8')

    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted = aes.encrypt(pad(input.encode(), BLOCK_SIZE))

    return hexlify(encrypted).decode("utf-8")


def decrypt(einput):
    key = bytes(CRYPTO_KEY, 'utf-8')
    iv = bytes(CRYPTO_IV, 'utf-8')

    einput = unhexlify(einput)
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(einput), BLOCK_SIZE).decode("utf-8")


def main():
    output = encrypt(input)
    plaintext = decrypt(output)

    print(output)
    print(plaintext)


if __name__ == "__main__":
    main()

