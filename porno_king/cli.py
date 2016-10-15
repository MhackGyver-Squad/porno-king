# -*- coding: utf-8 -*-
__author__ = """Mh@cKGyv3R"""
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.1.0'

import itertools
import sys
import click
import porno_king.scan as scanner
from porno_king.core.exceptions import KnockProtocoleError


@click.group()
def main(args=None):
    """Porno-King a port knocking sequence discovery scanner"""
    pass


@main.command()
@click.argument('ports', nargs=-1, type=str)
@click.argument('host', nargs=1)
@click.option('-t', '--timeout', type=float, default=0.1)
def scan(**kwargs):
    '''Test all sequences with specified PORTS on HOST'''
    ports = kwargs['ports']
    host = kwargs['host']
    try:
        for random_ports in itertools.permutations(ports):
            scanner.knock(random_ports, host)
        sys.exit(0)
    except KeyboardInterrupt:
        print('User abort ! Bye Dude')
        sys.exit(1)
    except KnockProtocoleError as kpe:
        print(str(kpe))
        sys.exit(1)


@main.command()
@click.argument('ports', nargs=-1, type=int)
@click.argument('host', nargs=1)
def knock(**kwargs):
    '''Open with specified PORTS on TARGET'''
    ports = kwargs['ports']
    host = kwargs['host']
    try:
        pass
        #open(ports, host)
    except KeyboardInterrupt:
        print('User abort ! Bye Dude')
        sys.exit(1)


@main.command()
def version():
    """Display Porno-King Version"""
    print('Porno-King {version}'.format(version=__version__),)


if __name__ == "__main__":
    main()
