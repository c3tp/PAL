import sys
from flask import Flask


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    print "Hi"

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])

if __name__ == '__main__':
    run()
