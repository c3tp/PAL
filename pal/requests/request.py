import random
import string

import boto3

import pal.authentication.auth_strategy as auth_strats
import pal.config.defaults as defaults


def generate_request(
        auth_strategy: auth_strats.AbstractAuthenticationStrategy,
        username: string,
        password: string):
    key_id, key = auth_strategy.authenticate(username, password)
    print("keys are %s: %s" % (key_id, key))
    s3_client = __generate_client(
        s3_endpoint_url=defaults.S3_ENDPOINT,
        key_id=key_id,
        key=key)
    __perform_a_bunch_of_actions(s3_client)


def __random_string(length=13):
    "Return a random string of given length"
    random.seed()
    return ''.join([
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
        ])


def __s3_bucket_name(prefix="c3tp-"):
    min_length = 3
    max_length = 63 - len(prefix)
    return prefix + __random_string(random.randint(min_length, max_length)).lower()


def __generate_client(s3_endpoint_url, key_id, key):
    return boto3.client(
        service_name="s3",
        endpoint_url=s3_endpoint_url,
        aws_access_key_id=key_id,
        aws_secret_access_key=key,
        verify=False)


def __perform_a_bunch_of_actions(s3_client):
    bucket_name = __s3_bucket_name()
    response = s3_client.list_buckets()
    s3_client.create_bucket(Bucket=bucket_name)
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)
    s3_client.delete_bucket(Bucket=bucket_name)


def test_request():
    '''Create a bucket and try to list out all buckets, then delete it'''
    print("Testing requests")
    s3_client = boto3.client(
        service_name="s3",
        endpoint_url=defaults.S3_ENDPOINT,
        verify=False)
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)