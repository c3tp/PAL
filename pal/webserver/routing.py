#!flask/bin/python

from flask import Flask, request, jsonify
from pal.config.defaults import WEBSITE_DEFAULT_DOMAIN
import sys
import string
import pal.requests.client as client
import pal.requests.presigned as presigned
import pal.requests.request as request
app = Flask(__name__)
app.config['SERVER_NAME'] = WEBSITE_DEFAULT_DOMAIN


@app.route('/')
def index():
    return "Index"


@app.route('/<string:key_name>/presigned_post', subdomain="<string:bucket_name>", methods=['GET'])
def get_presigned_post(bucket_name: string, key_name: string):
    print("presigned post: getting bucket:key %s : %s" % (bucket_name, key_name))
    presigned_post = presigned.get_presigned_upload(
        client.get_dummy_client(),
        bucket_name,
        object_key=key_name)
    return jsonify(presigned_post)


@app.route('/<string:key_name>/presigned_url', subdomain="<string:bucket_name>", methods=['GET'])
def get_presigned_url(bucket_name: string, key_name: string):
    print("presigned url: getting bucket:key %s : %s" % (bucket_name, key_name))
    return presigned.get_presigned_download(
        client.get_dummy_client(),
        bucket_name,
        object_key=key_name)


@app.route('/<string:key_name>', subdomain="<string:bucket_name>", methods=['POST'])
def put_object(bucket_name: string, key_name: string):
    print("putting object: bucket:key %s : %s" % (bucket_name, key_name))
    # TODO(Andreas): put an object. 
    return presigned.get_presigned_download(
        client.get_dummy_client(),
        bucket_name,
        object_key=key_name)


@app.route('/<string:key_name>', subdomain="<string:bucket_name>", methods=['GET'])
def get_object(bucket_name: string, key_name: string):
    print("getting object: bucket:key %s : %s" % (bucket_name, key_name))
    # TODO(Andreas): How do we process the object to be passed through? 
    return request.download_file(
        s3_client=client.get_dummy_client(),
        bucket=bucket_name,
        key=key_name)

# These paths are for fall through routing when we don't have something defined.


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', subdomain="<string:subdomain>")
def catch_all_subdomain(path, subdomain):
    return 'You want path: %s under subdomain: %s' % (path, subdomain)


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
