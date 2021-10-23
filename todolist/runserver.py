#!/usr/bin/env python

#----------------------------------------------------------------------
# runserver.py
# Authors: Julio Lins
#----------------------------------------------------------------------

from sys import exit, stderr
import argparse
from todolist import app
#-----------------------------------------------------------------------

def parse_arg():
    """Parse arguments."""

    descript = "The to-do list application"
    port_help = "the port at which the server should listen"

    parser = argparse.ArgumentParser(description = descript,
                                     allow_abbrev=False)

    parser.add_argument("port", help=port_help, type=int,
                        metavar="port")
    
    args = parser.parse_args()
    return args.port

def main():
    try:
        app.run(host='0.0.0.0', port=parse_arg(), debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


if __name__ == "__main__":
    main()