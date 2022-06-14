# Python 101 For Hackers


# Introduction

## Welcome and course introduction

![](assets/16552174225189.png)

## What is Python?
![](assets/16552177407235.png)


## Why learn Python as a hacker?

![](assets/16552178560639.jpg)


## Python2 vs Python3

![](assets/16552180490033.jpg)


# Setup

## How to install VirtualBox

* https://www.virtualbox.org

## How to install Kali Linux

* https://www.kali.org/get-kali/

## The Python interpreter

### Python3
![](assets/16552185037074.png)

### Python2
![](assets/16552185317724.png)


### Show Help

`python3 man`

![](assets/16552186336550.png)

### Run Code Snippet 

`python3 -c 'print("hello world")'`

![](assets/16552187403929.png)

### New Bash Session

`python3 -c 'print("hello world")'`

![](assets/16552188651086.png)

## How to run a Python script 

### Python 3

`python3 calculate-demo.py`

![](assets/16552190386479.png)


### Python 2

`python2 calculate-demo.py`

![](assets/16552191054775.jpg)

### Run it directly

```
#!/bin/python3
print(1 + 1)
```

after 

`chmod +x calculate-demo.py`

and 

`./calculate-demo.py`
![](assets/16552207324741.png)


### Optional Main Function

> If there is '__main__', this will be executed first

```
#!/bin/python3

print(1 + 1)
print(__name__)

if __name__ == "__main__":
    print("do something")
```

![](assets/16552210727579.jpg)


## Python syntax

> Always use same Indentation. For Example double space or tab. Mixing it inside a script will cause error.

![](assets/16552216894035.png)


### Official Python Documentation

* https://docs.python.org/3/
![](assets/16552219865059.png)

### Included Help in Python

#### Search Help for specific function

`python3`

![](assets/16552220456013.png)

`help(print)`

> *print* ins this case what I want so search in help

![](assets/16552221448939.png)

#### See arguments for specific function

`dir(print)`

![](assets/16552223851524.png)

### Python Style Guide

PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/v

