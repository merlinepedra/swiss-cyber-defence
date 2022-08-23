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
