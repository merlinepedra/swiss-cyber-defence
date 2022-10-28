#!/usr/bin/python3

import os
import sys
import re
import json
from collections import Counter, OrderedDict


accessLogName = "access.log"

if __name__ == '__main__':

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

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

  









