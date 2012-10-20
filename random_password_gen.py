#! /usr/bin/env python

''' Class based random password generator.  Uses string, random, sys modules. '''

__author__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Development" # __status__  one of "Prototype", "Development", or "Production"
__date__ = "2012/10/20 16:51:54"

import random
import string
import sys

class RandomPassword(object):
    def __init__(self, len=20):
        self.len = len
    
    def password_gen(self):
        #remove all escape characters
        x = repr(string.printable.replace(' \t\n\r\x0b\x0c',''))
        s = ''
        for i in range(self.len):
            s += random.choice(x)
        return s

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print RandomPassword(int(sys.argv[1])).password_gen()
    else:
        print RandomPassword().password_gen()