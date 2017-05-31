import sys
import pal.authentication.auth_handler as auth_handler


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    result = auth_handler.do_some_adding(1, 2)
    print("Hi")
    print("Calling the abstract method generate a %d" % result)


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])

if __name__ == '__main__':
    run()
