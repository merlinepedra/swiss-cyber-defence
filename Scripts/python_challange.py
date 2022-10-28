#!/usr/bin/python3

import os
import sys
import re
import json
from collections import Counter, OrderedDict
import random
import string

def parseLogAndCountIPs(accessLogName):
    try:
        file = open(accessLogName)
    except:
        print("File not found: {}", accessLogName)

    # get all ip matches
    ips = []
    for line in file:
        result = re.match(r"^([0-9]{1,3}(?:\.[0-9]{1,3}){3}) -", line)
        if result:
            ips.append(result.group(1))

    
    # create ordered mapping of counts
    orderedIps = OrderedDict(Counter(ips).most_common())

    # write json file
    with open("./results.json", "w") as jsonFile:
        json.dump(orderedIps, jsonFile, indent=2)
    
    print("Successfully aggregated log and wrote result.json")


def randAscii(length):
    """Generate a random string"""
    str = string.ascii_letters
    return ''.join(random.choice(str) for i in range(length)) 


if __name__ == '__main__':

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    parseLogAndCountIPs("access.log")
    print(randAscii(10))
    