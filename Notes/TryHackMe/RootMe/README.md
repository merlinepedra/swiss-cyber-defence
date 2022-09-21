

Nmap Scan
nmap -sV -v -oN  nmap.txt --script vuln -T5 -p-  10.10.21.89 


Enumerate Dirs
gobuster dir --wordlist /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt --url http://10.10.21.89


http://10.10.21.89/uploads
http://10.10.21.89/panel


PHP Upload Restriction bypass:
https://pentestlab.blog/2012/11/29/bypassing-file-upload-restrictions/
