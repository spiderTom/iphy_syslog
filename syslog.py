

import os
import sys


def seperate(filename):
    with open(filename, 'r') as source:
        with open("syslog"+filename, 'w') as dest:
            for line in source:
                if line.find("/I-PHY/") != -1:
                    dest.write(line)

print sys.argv
if len(sys.argv) < 2:
    print "please input source file name!"
else:
    seperate(sys.argv[1])


