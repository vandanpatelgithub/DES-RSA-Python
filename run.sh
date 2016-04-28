#!/bin/sh

python cipher.py DES abcdef0123456789 ENC input.txt output.txt

python cipher.py DES abcdef0123456789 DEC output.txt input.txt