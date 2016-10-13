# -*- coding: utf-8 -*-
__author__ = """Mh@cKGyv3R"""
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.1.0'

import itertools
import sys
import click
from porno_king.scan import knock


@click.group()
def main(args=None):
    """Porno-King a port knocking sequence discovery scanner"""
    pass


@main.command()
@click.argument('ports', nargs=-1, type=int)
@click.argument('host', nargs=1)
def scan(**kwargs):
    '''Test all sequences with specified PORTS on TARGET'''
    ports = kwargs['ports']
    host = kwargs['host']
    try:
        for random_ports in itertools.permutations(ports):
            knock(random_ports, host)
    except KeyboardInterrupt:
        print('User abort ! Bye Dude')
        sys.exit(1)


@main.command()
def version():
    """Display Porno-King Version"""
    print('Porno-King {version}'.format(version=__version__),)


if __name__ == "__main__":
    main()
