

Port Mirroring:

``` 
ovs-vsctl -- --id=@p get port tap101i1 \
    -- --id=@m create mirror name=span1 select-all=true output-port=@p \
    -- set bridge vmbr2 mirrors=@m
```



[https://bilk0h.com/posts/security-onion-proxmox-open-vswitch](https://bilk0h.com/posts/security-onion-proxmox-open-vswitch)

---

In Shell of Proxmox Server:

daemonlogger -i enp8s0 -o vmbr2

![[Pasted image 20230321164817.png]]

![[Pasted image 20230321164844.png]]