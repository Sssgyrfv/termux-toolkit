#!/bin/python

import hashlib

text = raw_input("\033[00m[\033[1;31m+\033[00m] Text\033[1;31m: \033[0;36m")
wow = hashlib.new('md4')
wow.update(text)
md4 = wow.hexdigest()
print "\033[00m[\033[1;32m+\033[00m] MD4\033[1;31m: \033[0;33m"+md4
