import cipherInterface
import sys
from Crypto.Cipher import DES


class myDES(cipherInterface.CipherInterface):

    final_key = ""
    plaintext = ""
    ciphertext = ""

    def __init__(self):
        print("you are in DES!")

    def setKey(self, key):

        if len(key) != 16:

            print("Key has to be exactly 16 characters")
            sys.exit()

        for (char1, char2) in zip(key[0::2], key[1::2]):

            self.final_key += chr(int(char1+char2,16))

        return self.final_key

    def encrypt(self, plainText):

        print("Encrypting...")

        if len(plainText) != 8:

            print("block has to be exactly 8 characters")

            sys.exit()


        des = DES.new(self.final_key, DES.MODE_ECB)

        self.ciphertext = des.encrypt(plainText)

        return self.ciphertext

    def decrypt(self, cipherText):

        print("Decrypting...")

        if len(cipherText) != 8:

            print("block has to be exactly 8 characters")

            sys.exit()

        des = DES.new(self.final_key, DES.MODE_ECB)

        self.plaintext = des.decrypt(cipherText)

        return self.plaintext




