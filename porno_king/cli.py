# -*- coding: utf-8 -*-
__author__ = """Mh@cKGyv3R"""
__email__ = 'herveberaud.pro@gmail.com'
__version__ = '0.1.0'

import itertools
import sys
import click
import porno_king.scan as scanner
import porno_king.knock as opener
from porno_king.core.exceptions import KnockProtocoleError


@click.group()
def main(args=None):
    """Porno-King a fully port knocking tools"""
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
    '''Send specified sequence on HOST'''
    ports = kwargs['ports']
    host = kwargs['host']
    try:
        pass
        opener(ports, host)
    except KeyboardInterrupt:
        print('User abort ! Bye Dude')
        sys.exit(1)
    except KnockProtocoleError as kpe:
        print(str(kpe))
        sys.exit(1)


@main.command()
def version():
    """Display Porno-King Version"""
    print('Porno-King {version}'.format(version=__version__),)


@main.command()
def credits():
    """Display Porno-King Credits"""
    print("""
   ___                         __ ___          
  / _ \___  _______  ___  ____/ //_(_)__  ___ _
 / ___/ _ \/ __/ _ \/ _ \/___/ ,< / / _ \/ _ `/
/_/   \___/_/ /_//_/\___/   /_/|_/_/_//_/\_, / 
                                        /___/` 
    """)
    print('Created by the MhackGyver pentest team')
    print('Main developer: 4383 - https://github.com/4383\n')


if __name__ == "__main__":
    main()
