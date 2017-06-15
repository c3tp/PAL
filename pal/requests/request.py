#!/usr/bin/env python3

import random
import string
import boto3
import pal.authentication.auth_strategy as auth_strats
import pal.requests.client as client


def download_file(s3_client: boto3.client, bucket, key):
    "Using an existing client, return a file from a bucket"
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    return s3_object


def upload_file(s3_client: boto3.client, bucket, key, fileobject):
    s3_client.upload_file(fileobject, bucket, key)

