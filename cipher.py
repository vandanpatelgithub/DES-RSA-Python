import sys
from myDES import myDES
from myRSA import myRSA

ciphers = { 'DES' : 'Data Encryption Standard', 'RSA' : 'Rivest, Shamir, & Adleman', 'CBC' : 'Cipher Block Chaining'}

activities = {'ENC', 'DEC'}

outputText = ""
cipherArray = []
cipherDESArray = []

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

            with open(inputFile, 'r') as f:
                while True:
                    block = f.read(8)
                    if not block:
                        break

                    while len(block) < 8:
                        block += "0"

                    fileWriter.write(cipher.encrypt(block))

        elif cipherName == 'RSA':

            cipher = myRSA()

            cipher.setKey(cipherKey)

            with open(inputFile, 'r') as f:
                while True:
                    block = f.read(PLAIN_TEXT_BLOCK_SIZE)
                    if not block:
                        break
                    fileWriter.write(cipher.encrypt(block))

        elif cipherName == "CBC":

            cipher = myDES()

            IV = raw_input("Please enter Initialization Vector : ")

            if len(IV) == 0:
                print("Initialization Vector cannot be empty!")

            elif len(IV) != 16:
                print("Initialization Vector has to be 16 charactes (8 bytes)")

            else:

                iv_to_list = cipher.iv_to_int(IV)

                counter = 0

                cipher.setKey(cipherKey)

                with open(inputFile, 'r') as f:
                    while True:
                        block = f.read(8)
                        if not block:
                            break

                        while len(block) < 8:
                            block += "0"

                        if counter == 0:

                            block_to_list = cipher.block_to_int(block)

                            char_list = cipher.xor_list(iv_to_list, block_to_list)

                            print("Encrypting in CBC Mode ...")

                            cipherText = cipher.encrypt(''.join(char_list))

                            cipherArray.append(cipherText)

                            counter += 1

                            fileWriter.write(cipherText)

                        else:


                            ciphertext_list = cipher.block_to_int(cipherText)

                            plaintext_list = cipher.block_to_int(block)

                            char_list = cipher.xor_list(ciphertext_list, plaintext_list)

                            print("Encrypting in CBC Mode ...")

                            cipherText = cipher.encrypt(''.join(char_list))

                            cipherArray.append(cipherText)

                            fileWriter.write(cipherText)


    elif activity == "DEC":

        if cipherName == 'DES':

            cipher = myDES()
            cipher.setKey(cipherKey)

            with open(inputFile, 'r') as f:
                while True:
                    block = f.read(8)
                    if not block:
                        break

                    fileWriter.write(cipher.decrypt(block))

        elif cipherName == 'RSA':

            cipher = myRSA()

            cipher.setKey(cipherKey)

            with open(inputFile, 'r') as f:
                while True:
                    block = f.read(CIPHER_TEXT_BLOCK_SIZE)
                    if not block:
                        break
                    fileWriter.write(cipher.decrypt(block))

        elif cipherName == "CBC":

            cipher = myDES()

            IV = raw_input("Please enter Initialization Vector : ")

            if len(IV) == 0:
                print("Initialization Vector cannot be empty!")

            elif len(IV) != 16:
                print("Initialization Vector has to be 16 charactes (8 bytes)")

            else:

                iv_to_list = cipher.iv_to_int(IV)

                counter = 0

                cipher.setKey(cipherKey)

                with open(inputFile, 'r') as f:

                    while True:
                        block = f.read(8)
                        if not block:
                            break

                        while len(block) < 8:
                            block += "0"

                        if counter == 0:

                            previous_block = block

                            print("Decrypting in CBC Mode ...")

                            decryptedText = cipher.decrypt(block)

                            decryptedtext_to_list = cipher.block_to_int(decryptedText)

                            char_list = cipher.xor_list(decryptedtext_to_list, iv_to_list)

                            plaintext = ''.join(char_list)

                            counter += 1

                            fileWriter.write(plaintext)

                        else:

                            print("Decrypting in CBC Mode ...")

                            decryptedText = cipher.decrypt(block)

                            decryptedtext_to_list = cipher.block_to_int(decryptedText)

                            previous_block_to_list = cipher.block_to_int(previous_block)

                            char_list = cipher.xor_list(decryptedtext_to_list, previous_block_to_list)

                            plaintext = ''.join(char_list)

                            previous_block = block

                            fileWriter.write(plaintext)


    fileReader.close()
    fileWriter.close()
