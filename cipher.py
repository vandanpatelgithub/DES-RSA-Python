import sys
from myDES import myDES


ciphers = { 'DES' : 'Data Encryption Standard'}

activities = {'ENC', 'DEC'}

cipher = myDES()

cipher.setKey("1234567890abcdef")

ciphertext = cipher.encrypt("vandanpr")

print(ciphertext)

plaintext = cipher.decrypt(ciphertext)

print(plaintext)

if len(sys.argv) < 6:

    print("You haven't entered the input correctly!")

    print("Correct Input = python cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUT-FILE> <OUTPUT-FILE>")

else:

    cipherName = sys.argv[1]

    cipherKey = sys.argv[2]

    activity = sys.argv[3]

    inputFile = sys.argv[4]

    outputFile = sys.argv[5]

    fileReader = open(inputFile, 'r')

    fileWriter = open(outputFile, 'w')

    if not (cipherName in ciphers.keys()):
        print("Valid Ciphers are : ")
        for key, value in ciphers.items():
            print(key, value)

    elif activity == "ENC":

        if cipherName == 'DES':

            cipher = myDES()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            cipherText = cipher.encrypt(text)
            fileWriter.write(cipherText)
            fileReader.close()
            fileWriter.close()

    elif activity == "DEC":

        if cipherName == 'DES':
            cipher = myDES()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            plainText = cipher.encrypt(text)
            fileWriter.write(plainText)
            fileReader.close()
            fileWriter.close()
