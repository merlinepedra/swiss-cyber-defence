# Snort

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