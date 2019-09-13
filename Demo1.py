import sys
import getopt
import re

arg, opt = getopt.getopt(sys.argv[1:], '-h:-o')
print(arg[0][1])
url = arg[0][1]


def checkURL(url):
    if re.match('b|a', url):
        print("ok")
    else:
        print("failed")


checkURL(url)
