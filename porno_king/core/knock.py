# -*- coding: utf-8 -*-
import socket
from porno_king.core.exceptions import KnockProtocoleError

TCP = 'tcp'
UDP = 'udp'

PROTOCOLES = {
    TCP: socket.SOCK_STREAM,
    UDP: socket.SOCK_DGRAM
}


def send_packet(port, host, timeout=0.1):
    port, protocole = get_port_and_protocole(port)
    try:
        s = socket.socket(socket.AF_INET, protocole)
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
    except socket.error as e:
        pass


def get_port_and_protocole(port):
    if ':' not in port:
        return int(port), PROTOCOLES[TCP]
    port, proto = port.split(':')
    if proto != TCP and proto != UDP:
        raise KnockProtocoleError("Bad protocole for {0} port".format(port))
    return int(port), PROTOCOLES[proto]


def port_is_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s.connect_ex((host, port)) == 0

