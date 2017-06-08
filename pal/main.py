import sys
import pal.requests.request as pal_request
import pal.authentication.dummy_strategy as dummy_strategy
import pal.requests.presigned as pal_presigned
import pal.requests.client as pal_client
import argparse


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='pre_upload/pre_download/upload/download')
    parser.add_argument('bucket')
    parser.add_argument('key')
    parser.add_argument('--username', default="lol", help='username help')
    parser.add_argument('--password', default="wut")
    parser.add_argument('--dummy-auth', default=True, action="store_true")
    args = vars(parser.parse_args())
    print("Hi we tried parsing")
    if args['dummy_auth'] is False:
        # TODO(Andreas): We'll do real auth eventually
        return

    print("we want to do dummy auth")
    strategy = dummy_strategy.DummyAuthenticationStrategy()
    client = pal_client.get_client(strategy, args['username'], args['password'])

    result = {
        'pre_upload': lambda b, k: pal_presigned.get_presigned_upload(client, b, k),
        'pre_download': lambda b, k: pal_presigned.get_presigned_download(client, b, k)
    }[args['command']](args['bucket'], args['key'])
    return result


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    run()
