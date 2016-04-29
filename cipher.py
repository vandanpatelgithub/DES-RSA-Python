import sys
from myDES import myDES
from myRSA import myRSA

ciphers = { 'DES' : 'Data Encryption Standard', 'RSA' : 'Rivest, Shamir, & Adleman'}

activities = {'ENC', 'DEC'}

outputText = ""

# The plaintext block
PLAIN_TEXT_BLOCK_SIZE = 214

# The ciphertext block
CIPHER_TEXT_BLOCK_SIZE = 256

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

    if not (activity in activities):
        print("Valid activities are : ")
        for activity in activities:
            print(activity)

    elif activity == "ENC":

        if cipherName == 'DES':

            cipher = myDES()
            cipher.setKey(cipherKey)

            text = fileReader.read()
            length = len(text)

            if length == 0:
                print("Your input file cannot be empty.")
                exit(1)

            elif length % 8 != 0:
                print("One of your plaintext blocks appears to have block size less than 8 byes. ALL BLOCKS HAVE TO BE 8 BYTES EXACTLY.")
                exit(1)

            else:

                with open(inputFile, 'r') as f:
                    while True:
                        block = f.read(8)
                        if not block:
                            break
                        outputText += cipher.encrypt(block)

            fileWriter.write(outputText)

        elif cipherName == 'RSA':

            cipher = myRSA()

            cipher.setKey(cipherKey)

            text = fileReader.read()
            length = len(text)

            if length == 0:
                print("Your input file cannot be empty")
                exit(1)

            else:

                with open(inputFile, 'r') as f:
                    while True:
                        block = f.read(PLAIN_TEXT_BLOCK_SIZE)
                        if not block:
                            break
                        outputText += cipher.encrypt(block)

            fileWriter.write(outputText)

    elif activity == "DEC":

        if cipherName == 'DES':
            cipher = myDES()
            cipher.setKey(cipherKey)

            text = fileReader.read()
            length = len(text)

            if length == 0:
                print("Your input file cannot be empty.")
                exit(1)

            elif length % 8 != 0:
                print("One of your plaintext blocks appears to have block size less than 8 byes. ALL BLOCKS HAVE TO BE 8 BYTES EXACTLY.")
                exit(1)

            else:
                with open(inputFile, 'r') as f:
                    while True:
                        block = f.read(8)
                        if not block:
                            break
                        outputText += cipher.decrypt(block)

            fileWriter.write(outputText)

        elif cipherName == 'RSA':

            cipher = myRSA()

            cipher.setKey(cipherKey)

            text = fileReader.read()
            length = len(text)

            if length == 0:
                print("Your input file cannot be empty")
                exit(1)

            else:

                with open(inputFile, 'r') as f:
                    while True:
                        block = f.read(CIPHER_TEXT_BLOCK_SIZE)
                        if not block:
                            break
                        outputText += cipher.decrypt(block)

            fileWriter.write(outputText)

    fileReader.close()
    fileWriter.close()
