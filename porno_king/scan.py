# -*- coding: utf-8 -*-
__author__ = 'TotoLeHero'
import socket
import time
import sys
pause = 1


def test_port(port, host):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((host, port))
        s.close()
    except socket.error as e:
        pass


def port_is_open(host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s.connect_ex((host, 22)) == 0


def knock(ports, host):
    sequence = ' '.join(str(port) for port in ports)
    print('Testing port sequence {0}'.format(sequence))
    for port in ports:
        test_port(port, host)

    time.sleep(0.5)
    if port_is_open(host):
        print('Port 22 is open. The right port sequence is {0}.'.format(sequence))
        sys.exit(0)
    print('Bad port sequence! Waiting {} seconds ' \
          'before trying another ports sequence...\n'.format(pause))
    time.sleep(pause)
