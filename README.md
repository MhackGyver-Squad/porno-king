# Porno-King
Port Knocking Security Utilities

![alt text](https://github.com/mhackgyver-squad/porno-king/blob/master/static/ron-jeremy-porno-king.jpg?raw=true "Ron Jeremy The Porno king !")

Dedicated to [Ron Jeremy](https://en.wikipedia.org/wiki/Ron_Jeremy) ! Thank you dude !

Full documentation are available [here](https://github.com/mhackgyver-squad/porno-king/wiki).

## Features
- Scan any host to discover hidden sequence (brute force).
- Send sequence on specified host like a simple port knocking client.
- Testing Server embedded (docker image) included: firewall reject all connections, ssh server running, port knocking daemon running.

## Current production release
Porno-king v0.2.3

## Installation
### From pypi
```shell
$ pip install porno-king
```
Classical installation
```shell
$ git clone https://github.com/mhackgyver-squad/porno-king
$ cd porno-king
$ python setup.py install
```

Development installation
```shell
$ git clone https://github.com/mhackgyver-squad/porno-king
$ cd porno-king
$ git checkout origin/development
$ pyvenv . # You can also use virtualenv it's work
$ source bin/activate
$ pip install -r requirements_dev.txt
$ python setup.py develop
$ # Now you can develop and use `$ porn <command>` directly in your shell
```

## Usages
Brute force mode to discover an hidden sequence
```shell
$ # Scan function help
$ porn scan --help
$ porn scan [PORTS]... [HOST]
$ # Example for scanning localhost with sequence 11 12 13
$ porn scan 11 12 13 127.0.0.1
```
Simple port knocking client mode for sending sequence
```shell
$ porn knock 11 12 13 127.0.0.1
```

You can also specify protocole to use (TCP/UDP) with each ports
Example:
```shell
$ porn scan 7000:tcp 8000:udp 9000:tcp 127.0.0.1
```

If protocole is not specified on port TCP are used by default.
If port to test during a scan with the option -p is not specified port 22 (SSH) is tested by default.

## Embedded server
Use the embedded server for test your development on it.

Start from docker hub
```shell
$ docker pull 4383/porno-king
```

Start from local Dockerfile
```shell
$ cd server
$ docker build -t porno-king-server .
$ docker run --privileged porno-king-server
$ # get the ip address of the porno-king-server
$ docker inspect porno-king-server # retrieve IP on command output
$ # suppose IP is equal to 172.17.0.2
$ porn scan 7000 8000 9000 172.17.0.2
```
You can also use this server to play and discover port-knocking mechanism

### Embedded server open sequence
7000 8000 9000

### Embedded server close sequence
9000 8000 7000 

## Roadmap (Next features)
- Publish porno-king on Pypi
- Publish porno-king-server on docker hub
- Provide sequence/host storage in local sqlite database

## Dependances
- [clic](http://click.pocoo.org/6/)

## Credits
Authors: [Mh@cKGyv3R](https://mhackgyver-squad.github.io/mhackgyver/)
