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

