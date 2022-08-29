# Practical Web Application Security and Testing


# 0: Prologue

## 0-1: Welcome
![](assets/16554457963165.png)

![](assets/16554458860588.png)

![](assets/16554459378717.png)

## 0-2: About the Instructor


## 0-3: Course Structure

![](assets/16554460384428.png)

![](assets/16554460290382.png)

# 1: Setup

## 1-1: Lab Setup Overview

* Ubuntu Server
* Windows Machine

## 1-2: Lab Setup - Hyper-V

## 1-4: Lab Setup - Kali Linux

> git clone https://github.com/mttaggart/pwst-resources
> cd ~/pwst-resources/kali-setup
> ./setup.sh


`sudo kali-tweaks`

[Install Brave Browser](https://brave.com/linux/#release-channel-installation)
> Brave doesn't support currently ARM64


### Install Some tools on Kali

`sudo apt install -y fish terminator gedit python3-pip vim-gtk-3`

### Clone latest **SecLists** to "Scripts" Folder

`git clone https://github.com/danielmiessler/SecLists`

### Install Rush

https://rustup.rs/

`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

Add in terminal:
`source $HOME/.cargo/env`

### Install rustscan (Very fast Port Scanner)

└─$ cargo install rustscan

### Install feroxbuster (Perform Forced Browsing)

└─$ cargo install feroxbuster    

### Install powerline fonts

`git clone https://github.com/powerline/fonts`

`./install`

### Terminator

open **Terminator** Terminal

### oh-my-fish

`curl -kL https://get.oh-my.fish`

`exit`

`fish -c "omf install bobthefish"`

`echo "set -x PATH \$PATH $HOME/.cargo/bin" >> ~/.config/fish/config.fish`

`chsh -s /usr/bin/fish`

##  1-5: Lab Setup - Docker

### On Kali Machine:

`sudo pico /etc/hosts`

Add

`10.211.55.12   pwst-server`


### On Server

Install Docker: https://docs.docker.com/engine/install/ubuntu/


### Add my User to docker group

> Bad idea for real life!

`sudo gpasswd -a iceman docker`


# 2: Web Application Concepts

## 2-1: Servers and Clients

![](assets/16554622952267.png)
![](assets/16554623411599.png)


## 2-2: Lab - Nginx and Server Logs

### Install nginx via Docker

`docker image pull nginx`

`docker image ls`

`docker container run --rm -p 80:80 nginx`

### Request via curl

`curl http://pwst-server/`


![](assets/16554626966647.png)


`curl http://pwst-server/test`

### Request via netcat

`nc pwst-server 80`

> "Enter" twice

![](assets/16554629915218.png)


##  2-3: HTTP

![](assets/16554633850011.png)

![](assets/16554634487293.png)

![](assets/16554635360822.png)

![](assets/16554635840218.png)


### curl verbose

`curl -v https://swiss-cyber-defence.ch`

![](assets/16554637577757.png)

`curl -v http://swiss-cyber-defence.ch`

![](assets/16554639404802.png)


`curl -X POST -v https://swiss-cyber-defence.ch/`

`curl -X POST -v https://swiss-cyber-defence.ch/ -H "User-Agent: PWST"`

##  2-4: The Web Trinity

`git clone https://github.com/mttaggart/pwst-resources`

Go to:
` ~/S/pwst-resources/2-4_web-trinity`

## 2-5: HTML

`file:///home/parallels/Scripts/pwst-resources/2-5_html/index.html`

* https://htmlreference.io/
* https://www.w3schools.com/tags/default.asp

## 2-6: CSS

`file:///home/parallels/Scripts/pwst-resources/2-6_css/index.html`

## 2-7: JavaScript

`file:///home/parallels/Scripts/pwst-resources/2-7_js/index.html`

## 2-8: Lab - Alert Button

![](assets/16554681986415.jpg)


## 2-9: ZAP Intro

`sudo apt install -y zaproxy`


### Change ZAP interface to Darkmode

![](assets/16554692120030.jpg)



### Install Browser Extensions

![](assets/16554685724962.png)



### Configure Proxy

![](assets/16554691132083.png)


![](assets/16554691535910.jpg)


![](assets/16554692677753.jpg)

Import Saved ZAP Certificate

### Configure ZAP

![](assets/16554693585564.jpg)


![](assets/16554693842061.jpg)

![](assets/16554694229828.jpg)


#### Set Testing Scope

![](assets/16554696348953.jpg)


#### Marketplace

![](assets/16554698601123.jpg)

#### Install ZAP Plugins

* Directory List v2.3
* Install Directory List v2.3 LC
* FuzzDB Files
* FuzzDB Offensive
* Python Scripting
* Custom Payloads
* JSON View
* JWT Support
* ViewState
* Community Scripts

#### Adjust Proxy Config

![](assets/16554702650773.jpg)


![](assets/16554703618612.jpg)


#### Adjust Global Alert Filters

![](assets/16554704735956.jpg)

#### Passiv Scan Rules

Disable Timestamp Disclousre

![](assets/16554705679413.jpg)


## 2-10: Lab - ZAP Enumeration

`docker container ls`

`docker container stop <name>`

![](assets/16554712890642.jpg)


#### Add Site to Test to Context & Run Spider

![](assets/16554715053413.jpg)


#### Inspect Source Code 

![](assets/16554717026200.jpg)


![](assets/16554716700414.jpg)


#### Fuzzing URLs

Select document name part of url and Fuzz

![](assets/16554721482335.jpg)


![](assets/16554723568840.jpg)


![](assets/16554725846381.jpg)


![](assets/16554726786629.jpg)

# 3: Server-Side Webapps

## 3-1: PHP

![](assets/16554727970856.jpg)


![](assets/16554728581205.jpg)


## 3-2: Lab - PHP with Docker

### Code Execution & Vulnerable for Cross Site Scripting

![](assets/16554737520352.jpg)



![](assets/16554737849576.jpg)


**Remote Code Execution**

`curl -v -X POST http://pwst-server:8000  -d "cmd=whoami"`

![](assets/16554740549722.jpg)



## 3-3: Server Side Security Considerations

![](assets/16554744273974.jpg)

![](assets/16554745281730.jpg)


![](assets/16554746714656.jpg)

![](assets/16554746877579.jpg)

![](assets/16554747688155.jpg)

![](assets/16554748697623.jpg)


![](assets/16554749312058.jpg)

## 3-4: Lab - Wordpress

`/pwst-resources/3-4_lab-wordpress`

> ARM64 Issue

![](assets/16554756440876.png)


### Fuzzer (Find Wordpress User to login)

![](assets/16554782315423.jpg)

![](assets/16554783761797.jpg)

![](assets/16554784277986.jpg)

![](assets/16554785017768.jpg)

> Do same again but this time use founded username and fuzz password


## Lab - DVWA

Go to:

`xxxx@pwst-server:~/pwst-resources/3-5_lab-dvwa$ `

then:

`docker compose up -d`

> If you run it on ARM64 Processor, add this to `docker-compose.yml`

```
 mysql:
    platform: linux/amd64
```

Check if everything started:

`docker container ls`

# The OWASP Top 10

## OWASP Overview

![](assets/16616690093784.jpg)

![](assets/16616690578232.jpg)

## 4-2: Broken Access Control

![](assets/16616713444069.jpg)

##  4-3: Cryptographic Failures

![](assets/16616714171457.jpg)


![](assets/16616720354841.jpg)

![](assets/16616720561518.png)

![](assets/16616720864788.jpg)

![](assets/16616717985280.jpg)

![](assets/16616718122013.jpg)

![](assets/16616718405632.jpg)

![](assets/16616719763549.jpg)

![](assets/16616719869506.jpg)

##  4-4: Injection - XSS

![](assets/16616721862523.jpg)

