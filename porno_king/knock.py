# -*- coding: utf-8 -*-
import socket
import time
import sys
from porno_king.core.knock import send_packet


def knock(ports, host):
    for port in ports:
        send_packet(port, host)
