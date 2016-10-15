# Porno-King
Port Knocking Sequence Discovery Scanner

![alt text](https://github.com/mhackgyver-squad/porno-king/blob/master/static/ron-jeremy-porno-king.jpg?raw=true "Ron Jeremy The Porno king !")

## Features
- Scan any host to discover hidden sequence (brute force)
- Testing Server embedded (docker image) included: firewall reject all connections, ssh server running, port knocking daemon running

## Installation
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
$ pyvenv . # You can also use virtualenv it's work
$ source bin/activate
$ python setup.py develop
$ # Now you can develop and use `$ porn <command>` directly in your shell
```

## Usages
```shell
$ # Scan function help
$ porn scan --help
$ porn scan [PORTS]... [HOST]
$ # Example for scanning localhost with sequence 11 12 13
$ porn scan 11 12 13 127.0.0.1
```

You can also specify protocole to use (TCP/UDP) with each ports
Example:
```shell
$ porn scan 7000:tcp 8000:udp 9000:tcp 127.0.0.1
```

If protocole is not specified on port TCP are used by default.

## Embedded server
Start the embedded server and test your development on it:
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

## Roadmap
- Publish porno-king on Pypi
- Publish porno-king-server on docker hub
- Provide a simple command knock like a traditionaly knocking client
- Provide sequence/host storage in local sqlite database

## Credits
Dedicated to [Ron Jeremy](https://en.wikipedia.org/wiki/Ron_Jeremy) ! Thank you dude !

Authors: Mh@cKGyv3R
