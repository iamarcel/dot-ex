#!/usr/bin/python

import crypt
import sys
import string
import random

# Generate random salt (16 chars, uppercase lowercase or digit
salt = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
print(salt)

# Encrypt password and print salt
pw = sys.argv[0]
print(crypt.crypt(pw, "$6$" + salt))
