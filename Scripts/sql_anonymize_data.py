#!/usr/bin/python3

import os
import binascii
import sqlite3
import random
import string

dbFilename = "customerdata.db"
originalTableName = "customers"
anonymizedTableName = "anonymizedData"

def encrypt(val,s):
    x = 2<<7
    n = 0
    p = s
    p = [ord(x) for x in p]
    var = []
    while n < x:
        var.append(n)
        n += 1
    t = 0
    t_n = len(p)
    n = 0
    while n < x:
        t = t + var[n] + p[n % t_n]
        t %= x
        t_s = var[n]
        var[n] = var[t]
        var[t] = t_s
        n += 1
    t_n = len(val)
    p = 0
    q = 0
    t_t = []
    for n in range(t_n):
        t_t.append(n)
    n=0
    while n < t_n:
        p += 1
        p %= x
        q += var[p]
        q %= x
        t_s = var[p]
        var[p] = var[q]
        var[q] = t_s
        t_r = var[p] + var[q]
        t_r %= x
        t_r = var[t_r]
        t_t[n]=(t_r^ord(val[n]))
        n += 1
    return ''.join(['%02x'%x for x in t_t]) 

def setRandomString(columnKey, length):
    """Generate a random string"""
    try:
        str = string.ascii_letters
        encrypted_values = []

        cwd = os.getcwd()
        conn = sqlite3.connect('{0}{1}{2}'.format(cwd, os.sep, dbFilename))
        c = conn.cursor()

        c.execute('''SELECT {} FROM {};'''.format(columnKey, anonymizedTableName))
        records = c.fetchall()

        for record in records:
            randomString =  ''.join(random.choice(str) for i in range(length))
            encrypted_values.append(randomString)

        rowId = 1
        for value in encrypted_values:
            c.execute('''UPDATE `{}` SET `{}`=\'{}\' WHERE id='{}';'''.format(anonymizedTableName, columnKey, value, rowId))
            rowId += 1
        conn.commit()
        conn.close()
    except Exception as e:
            print('Type: {0}; Issue: {1}'.format(type(e), e))

def setRandomNumer(columnKey, length):
    """Generate a random string"""
    try:
        str = string.digits
        encrypted_values = []

        cwd = os.getcwd()
        conn = sqlite3.connect('{0}{1}{2}'.format(cwd, os.sep, dbFilename))
        c = conn.cursor()

        c.execute('''SELECT {} FROM {};'''.format(columnKey, anonymizedTableName))
        records = c.fetchall()

        for record in records:
            randomString =  ''.join(random.choice(str) for i in range(length))
            encrypted_values.append(randomString)

        rowId = 1
        for value in encrypted_values:
            c.execute('''UPDATE `{}` SET `{}`=\'{}\' WHERE id='{}';'''.format(anonymizedTableName, columnKey, value, rowId))
            rowId += 1
        conn.commit()
        conn.close()
    except Exception as e:
            print('Type: {0}; Issue: {1}'.format(type(e), e))


def setStaticMasking(columnKey, keepLenght, astrixLenght):
    keepLenght = keepLenght + 1

    marking = ""
    for x in range(astrixLenght):
        marking = "{}*".format(marking)

    try:
        executeSQL('''UPDATE {3} SET {0} = substr({0}, 0, {1}) || '{4}'    ;'''.format(columnKey, keepLenght, astrixLenght, anonymizedTableName, marking))
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))


def reduceDate(columnKey, format):
    try:
        executeSQL('''UPDATE {2} SET {0} = strftime('{1}', {0});'''.format(columnKey, format, anonymizedTableName))
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))

def setCategory(columnKey, catName, condition):
    try:
        executeSQL('''UPDATE {3} SET {0} = '{1}' WHERE {0} {2} AND {0} NOT NULL;'''.format(columnKey, catName, condition, anonymizedTableName))
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))

def setNullValue(columnKey):
    try:
        executeSQL('''UPDATE {1} SET {0} = null;'''.format(columnKey, anonymizedTableName))
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))

def executeSQL(sql):
    cwd = os.getcwd()
    conn = sqlite3.connect('{0}{1}{2}'.format(cwd, os.sep, dbFilename))
    c = conn.cursor()
    c.execute('''{}'''.format(sql))
    conn.commit()
    conn.close()

def deleteExistingAnonymizedTable():
    try:
        executeSQL('''DROP TABLE {};'''.format(anonymizedTableName))
    except Exception as e:
        print("")


def duplicateTable():
    try:
        executeSQL('''CREATE TABLE {} AS SELECT * FROM {};'''.format(anonymizedTableName, originalTableName))
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))


def copyTableBack():
    try:
        executeSQL('''DROP TABLE {};'''.format(originalTableName))
        executeSQL('''CREATE TABLE {} AS SELECT * FROM {};'''.format(originalTableName ,anonymizedTableName))
        deleteExistingAnonymizedTable()
    except Exception as e:
        print('Type: {0}; Issue: {1}'.format(type(e), e))


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    deleteExistingAnonymizedTable()
    duplicateTable()
    setStaticMasking("firstname", 1, 20)
    setRandomString("lastname", 3)
    reduceDate("date_of_birth", "%Y")

    catField = "cc_cvv"
    setCategory(catField, "high", ">= 600")
    setCategory(catField, "medium", ">= 200 AND {} < 600".format(catField))
    setCategory(catField, "low", "< 200")

    setNullValue("cc_type")
    
    setRandomNumer("contract_id", 10)


    # copyTableBack()









