#!flask/bin/python

from flask import Flask
import sys
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello_world!"


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    app.run(debug=True)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    run()
