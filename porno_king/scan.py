# -*- coding: utf-8 -*-
import socket
import time
import sys
from porno_king.core.knock import send_packet
from porno_king.core.knock import port_is_open
pause = 1


def knock(ports, host, target_port, timeout):
    sequence = ' '.join(str(port) for port in ports)
    print('Testing port sequence {0}'.format(sequence))
    for port in ports:
        send_packet(port, host, timeout)

    time.sleep(0.5)
    if port_is_open(host, target_port):
        print('Port {1} is open. The right port sequence is {0}.'.format(sequence, target_port))
        sys.exit(0)
    print('Bad port sequence! Waiting {} seconds ' \
          'before trying another ports sequence...\n'.format(pause))
    time.sleep(pause)
