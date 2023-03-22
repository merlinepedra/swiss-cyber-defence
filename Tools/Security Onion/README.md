# Security Onion


# Tutorials

* [Set up Security Onion to monitor your Proxmox Home Lab](https://bilk0h.com/posts/security-onion-proxmox-open-vswitch)

* [Security Onion + Proxmox Testing: Will it sniff?](https://bilk0h.com/posts/security-onion-proxmox-testing)

* [Security Onion + Proxmox Testing: Endpoint Reporting](https://bilk0h.com/posts/security-onion-proxmox-endpoints)

* [Using IP Reputation list to alert for SolarWinds Sunburst activity in Security Onion](https://bilk0h.com/posts/security-onion-ip-rep-solarwinds)


# Troubleshooting:


## Change Proxmoy Network Brdige from **Switch** to **Hub**

* [Deploying Security Onion / Proxmox Port mirroring
](https://forum.proxmox.com/threads/deploying-security-onion-proxmox-port-mirroring.37036/)
* [How to configure a Linux Bridge to act as a Hub instead of a Switch](https://techglimpse.com/convert-linux-bridge-hub-vm-interospection/)



Proxmox Port Mirroring for Listen Interface in Security Onion:

**In Shell of Proxmox Server:**

``` 
ovs-vsctl -- --id=@p get port tap101i1     -- --id=@m create mirror name=span1 select-all=true output-port=@p     -- set bridge vmbr2 mirrors=@m

ovs-vsctl list Mirror

daemonlogger -i enp8s0 -o vmbr2
```

