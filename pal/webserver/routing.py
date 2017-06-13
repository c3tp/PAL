#!flask/bin/python

import string
import sys

from flask import Flask, jsonify, request, redirect, url_for

import pal.authentication.dummy_strategy as dummy_strategy
import pal.requests.client as client
import pal.requests.presigned as presigned
import pal.requests.request as pal_request
from pal.requests.target import SymlinkTargetSpec
import pal.config.defaults as defaults
import pal.requests.symlink as symlink
from pal.config.defaults import WEBSITE_DEFAULT_DOMAIN

app = Flask(__name__)
app.config['SERVER_NAME'] = WEBSITE_DEFAULT_DOMAIN


@app.route('/')
def index():
    return "Index"

# Add new routes for default grabs


@app.route('/<string:bucket_name>/<string:key_name>', methods=['POST'])
def download_object(bucket_name: string, key_name: string):
    print("downloading object")
    s3_client = __generate_client(request)
    presigned_download_url = presigned.get_presigned_download(
        s3_client,
        bucket_name,
        object_key=key_name
    )
    return redirect(location=presigned_download_url, code=303)

# Add new routes for presigned url requests, without direct download


@app.route('/<string:bucket_name>/<string:key_name>/presigned_post', methods=['POST'])
def get_presigned_post(bucket_name: string, key_name: string):
    print("presigned post: getting bucket:key %s : %s" % (bucket_name, key_name))
    s3_client = __generate_client(request)
    presigned_post = presigned.get_presigned_upload(
        s3_client,
        bucket_name,
        object_key=key_name)
    return jsonify(presigned_post)


@app.route('/<string:bucket_name>/<string:key_name>/presigned_url', methods=['POST'])
def get_presigned_url(bucket_name: string, key_name: string):
    print("presigned url: getting bucket:key %s : %s" % (bucket_name, key_name))
    s3_client = __generate_client(request)
    return presigned.get_presigned_download(
        s3_client,
        bucket_name,
        object_key=key_name
    )


@app.route('/<string:bucket_name>/<string:key_name>/symlink', methods=['POST'])
def build_symlink(bucket_name: string, key_name: string):
    if 'target' not in request.form:
        return "Invalid request, need targetkey and targetbucket for symlink"
    s3_client = __generate_client(request)
    mount_point = None if 'mount_point' not in request.form else request.form['mount_point']
    symlink_target = SymlinkTargetSpec(request.form['target'], mount_point)
    symlink_built = symlink.build_symlink(s3_client, bucket_name, key_name, symlink_target)
    if not symlink_built:
        return "Symlink was not built"
    return (
        "Symlink created for target(%s) from source(%s)"
        % (request.form['target'], key_name)
    )

# These paths are for fall through routing when we don't have something defined.


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', subdomain="<string:subdomain>")
def catch_all_subdomain(path, subdomain):
    return 'You want path: %s under subdomain: %s' % (path, subdomain)


def __generate_client(request):
    if 'username' in request.form and 'password' in request.form:
        strategy = dummy_strategy.DummyAuthenticationStrategy()
        print("signing in user: %s: %s" % (request.form['username'], request.form['password']))
        return client.get_client(strategy, request.form['username'], request.form['password'])
    else:
        return client.get_dummy_client()


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
