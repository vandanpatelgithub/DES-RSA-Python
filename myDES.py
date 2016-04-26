import cipherInterface
import sys
from Crypto.Cipher import DES


class myDES(cipherInterface.CipherInterface):

    final_key = ""

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

        if len(plainText) != 8:

            print("block has to be exactly 8 characters")

            sys.exit()

        print("Length is " + str(len(self.final_key)))

        des = DES.new(self.final_key, DES.MODE_ECB)

        return des.encrypt(plainText)

    def decrypt(self, cipherText):

        if len(cipherText) != 8:

            print("block has to be exactly 8 characters")

            sys.exit()

        des = DES.new(self.final_key, DES.MODE_ECB)

        return des.decrypt(cipherText)




