#!/bin/sh


python cipher.py RSA pubkey.pem ENC input.txt output.txt

python cipher.py RSA privkey.pem DEC output.txt input.txt