import cipherInterface
import rsa
import sys
from rsa import key, common
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

class myRSA(cipherInterface.CipherInterface):

    KEY_SIZE = 512

    cipherText = ""
    plainText = ""
    rsaKey = ""



    def __init__(self):
        print("You are in RSA!")

    def setKey(self, fileName):

        self.rsaKey = b64decode(open(fileName,"r").read())
        self.rsaKey = RSA.importKey(self.rsaKey)
        self.rsaKey = PKCS1_OAEP.new(self.rsaKey)

    def encrypt(self, plainText):

        print("Encryptin RSA ...")

        self.cipherText = self.rsaKey.encrypt(plainText)

        return self.cipherText

    def decrypt(self, cipherText):

        print("Decryptin RSA ...")

        self.plainText = self.rsaKey.decrypt(cipherText)

        return self.plainText