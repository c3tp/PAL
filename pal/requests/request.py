import random
import string
import boto3
import pal.authentication.auth_strategy as auth_strats
import pal.requests.client as client


def download_file(s3_client: boto3.client, bucket, key):
    "Using an existing client, return a file from a bucket"
    # TODO(Andreas)
    return "stub"


def upload_file(s3_client: boto3.client, bucket, key):
    # TODO(Andreas)
    return "stub"


def generate_request(
        auth_strategy: auth_strats.AbstractAuthenticationStrategy,
        username: string,
        password: string):
    __perform_a_bunch_of_actions(client.get_client(auth_strategy, username, password))


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


def __perform_a_bunch_of_actions(s3_client):
    bucket_name = __s3_bucket_name()
    response = s3_client.list_buckets()
    s3_client.create_bucket(Bucket=bucket_name)
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print("Bucket List: %s" % buckets)
    s3_client.delete_bucket(Bucket=bucket_name)

