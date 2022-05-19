# Python


# Python Scripts



## Helper Scripts

### ## Kali Setup

🚧 [Kali-Setup.py](assets/Kali-Setup.py)

## School related exercies

### Merge Log Files
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

#### Goal & Tasks

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

