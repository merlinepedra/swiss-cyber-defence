

Port Mirroring:

``` 
ovs-vsctl -- --id=@p get port tap101i1 \
    -- --id=@m create mirror name=span1 select-all=true output-port=@p \
    -- set bridge vmbr2 mirrors=@m
```


