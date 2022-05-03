# Snort

## What is Snort?

Snort is the foremost Open Source Intrusion Prevention System (IPS) in the world. Snort IPS uses a series of rules that help define malicious network activity and uses those rules to find packets that match against them and generates alerts for users.

Snort can be deployed inline to stop these packets, as well. Snort has three primary uses: As a packet sniffer like tcpdump, as a packet logger — which is useful for network traffic debugging, or it can be used as a full-blown network intrusion prevention system. Snort can be downloaded and configured for personal and business use alike.

## Installation

[Snort Website](https://www.snort.org)

## Setup

Start snort manually
sudo snort -k none -d -l /etc/snort/log -b -c /etc/snort/snort.confor 

service snort start

## Create Snort Rules

Sample custom Rule
/etc/snort/rules/custom.rules


![](Snort%202%20rule%20header.png)

### Here are our custom rules!
`
alert tcp $EXTERNAL_NET any ->  $HOME_NET 22 (msg:"Incoming SSH traffic"; flags:S; sid:10000;)
``alert tcp $HOME_NET any -> $EXTERNAL_NET 4444 (msg:"Possible C&C traffic"; sid:10001;)``alert tcp $HOME_NET any $EXTERNAL_NET 4444 (msg: "harmful content search"; content: "hacking"; sid:10002;)``alert tcp $HOME_NET any $EXTERNAL_NET 4444 (msg: "harmful content search"; content: "|68 61 63 6b 69 6e 67|"; sid:10003;)`