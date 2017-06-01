import sys
import pal.requests.request as pal_request
import pal.authentication.dummy_strategy as dummy_strategy


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    strategy = dummy_strategy.DummyAuthenticationStrategy()
    pal_request.generate_request(strategy, "lol", "wut")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])

if __name__ == '__main__':
    run()
