# Aircrack-ng

[Official Website](https://aircrack-ng.org)

## What is Aircrack-ng

Aircrack-ng is a complete suite of tools to assess WiFi network security.

It focuses on different areas of WiFi security:

* Monitoring: Packet capture and export of data to text files for further processing by third party tools
* Attacking: Replay attacks, deauthentication, fake access points and others via packet injection
* Testing: Checking WiFi cards and driver capabilities (capture and injection)
* Cracking: WEP and WPA PSK (WPA 1 and 2)

All tools are command line which allows for heavy scripting. A lot of GUIs have taken advantage of this feature. It works primarily on Linux but also Windows, macOS, FreeBSD, OpenBSD, NetBSD, as well as Solaris and even eComStation 2.

## Installation

* Pre-Installed on Kali Linux


## General Information

* As more clients connected in WiFi Network as more likly it is that you can catch Handshake
* As more strong signal / more near to WiFi Accesspoint, as more successfully it is to fetch handshake's

## How to use

**Stop NetworkManager to aviod problems with Aircrack-ng**
`sudo systemctl stop NetworkManager`

**List WiFi-Networks**
`sudo airodump-ng wlan0`

**Try to Fetch Handshake ans Store Handshake**
`sudo airodump-ng -c  6 --bssid  00:00:00:00:00:00 -w /home/parallels/Desktop/wlan/hack wlan0`

**Deauth Clients in Network**
`sudo aireplay-ng  --deauth 10 -a  00:00:00:00:00:00 wlan0`

**Cracking Handshake with Password List**
`aircrack-ng -b 00:00:00:00:00:00 -w  /usr/share/seclists/Passwords/WiFi-WPA/probable-v2-wpa-top4800.txt Desktop/hack-07.cap`

**Start NetworkManager again. If you still can't connect to your Network, restart OS**
`sudo service network-manager start`


