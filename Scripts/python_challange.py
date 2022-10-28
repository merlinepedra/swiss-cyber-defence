#!/usr/bin/python3

import os
import binascii
import sqlite3
import random
import string

dbFilename = "customerdata.db"
originalTableName = "customers"
anonymizedTableName = "anonymizedData"

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

  









