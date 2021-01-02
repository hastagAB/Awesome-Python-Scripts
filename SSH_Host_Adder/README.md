# SSH Host adder

This is a fairly simple script which adds hosts to an ssh config file. 
SSH allows you to add hosts to a config file, so you don't have to remember ip addresses or hostnames. So if you add: 

```
HOST test
    HostName 192.168.80.1
    User root
    Port 22
```

to `~/.ssh/config`, you can just do `ssh test` instead of writing the address / user / port. 

But when you constantly get new servers to ssh to, it's helpful to have a script!

## Usage: 

```
./ssh_adder my_host 192.168.80.1 [--user myuser] [--port 2200]
```

`--user` and `--port` are optional and default to `root` and `22` respectively. 

If you aren't using the default ssh config path, there is an argument for that as well: 

```
./ssh_adder my_host 192.168.80.1 --conf /path/to/config
```

`-conf` defaults to `~/.ssh/config`

SSH configs allow you to make more complex operations, like adding different keys and whatnot, which I don't support here mostly because I haven't had a need to yet. If I get to updating my script some time, I'll update it here too. 
