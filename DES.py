import cipherInterface
import pyDes

class DES(cipherInterface.CipherInterface):

    def __init__(self):
        print("you are in DES!")

    def setKey(self, key):

        return 0


    def charToHex(self, char):

        if '0' <= char <= '9':

            return hex(int(char))

        elif 'a' <= char <= 'f':

            hexValue = ord(char) - 97

            return hex(hexValue + 10)

        elif 'A' <= char <= 'F':

            hexValue = ord(char) - 65

            return hex(hexValue + 10)

        else:

            return 'z'

    def twoCharToHexByte(self, chars):

        firstByte = self.charToHex(chars[0])

        secondByte = self.charToHex(chars[1])

        i = int(firstByte,16)

        j = int(secondByte,16)

        shifted = i << 4

        return hex(shifted | j)