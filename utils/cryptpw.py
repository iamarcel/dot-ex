#!/usr/bin/python3

import crypt
import sys
import string
import random

salt = crypt.mksalt(crypt.METHOD_SHA512)
pw = sys.argv[1]
print(crypt.crypt(pw, salt))
