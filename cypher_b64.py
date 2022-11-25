#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

input = '80:c9:55:64:73:f0'
CRYPTO_KEY= '8ookgvdIiH2YOgBnAju6Nmxtp14fn8d3'
CRYPTO_IV= 'rBEssDfxofOveRxR'

BLOCK_SIZE = 16


def encrypt(data):
    key = bytes(CRYPTO_KEY, 'utf-8')
    iv = bytes(CRYPTO_IV, 'utf-8')

    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted = aes.encrypt(pad(data.encode(), BLOCK_SIZE))
    
    # Make sure to strip "=" padding since urlsafe-base64 node module strips "=" as well
    return base64.urlsafe_b64encode(encrypted).decode("utf-8").rstrip("=")


def decrypt(edata):
    key = bytes(CRYPTO_KEY, 'utf-8')
    iv = bytes(CRYPTO_IV, 'utf-8')

    # Add "=" padding back before decoding
    edata = base64.urlsafe_b64decode(edata + '=' * (-len(edata) % 4))
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(edata), BLOCK_SIZE).decode("utf-8")


def main():
    output = encrypt(input)
    plaintext = decrypt(output)

    print(output)
    print(plaintext)


if __name__ == "__main__":
    main()

