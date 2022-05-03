# Volatility


**How to install**

By default Volatility isn't installed on Kali Linux.

## Volatility Procedure 

### 1. Identify rogue processes


Identify Operation System: 👨‍💻 vol.py -f target.img imageinfo

➡️ Now replace profile we found with  ‘MY_TARGET_PROFILE’

-------------------------

Print all running processes within the EPROCESS doubly linked list: 👨‍💻 vol.py -f target.img --profile=MY_TARGET_PROFILE  pslist

-------------------------

Print all running processes within the EPROCESS doubly linked list: 👨‍💻 vol.py -f  target.img --profile=MY_TARGET_PROFILE pslist

-------------------------

Scan physical memory for EPROCESS pool allocations:
👨‍💻vol.py -f target.img --profile=MY_TARGET_PROFILE psscan

-------------------------

Print process list as a tree showing parent relationship (using EPROCESS linked list):
👨‍💻vol.py -f target.img --profile=MY_TARGET_PROFILE pstree

-------------------------

Automatically identify suspicious system processes:
👨‍💻vol.py -f target.img --profile=MY_TARGET_PROFILE malprocfind

-------------------------

Compare processes and loaded DLLs with a basline image
👨‍💻vol.py -f target.img --profile=MY_TARGET_PROFILE processbl

-------------------------



### 2. Analyze process DLLs and handles


### 3. Review network artifacts


### 4. Look for evidence of code injection



### 5. Check for signs of a rootkit




### 6. Dump suspicious processes and drivers
