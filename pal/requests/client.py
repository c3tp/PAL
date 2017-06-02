#!/usr/bin/env python

import boto3
import pal.config.defaults as defaults
import pal.authentication.auth_strategy as auth_strats
import string


def get_client(
        auth_strategy: auth_strats.AbstractAuthenticationStrategy,
        username: string,
        password: string):
    key_id, key = auth_strategy.authenticate(username, password)
    print("keys are %s: %s" % (key_id, key))
    return get_wos_client(
        key_id=key_id,
        key=key)


def get_wos_client(key_id, key):
    return get_raw_boto_client(
        s3_endpoint_url=defaults.S3_ENDPOINT,
        key_id=key_id,
        key=key)


def get_raw_boto_client(s3_endpoint_url, key_id, key):
    """
    generates a client based on an endpoint, key_id, key
    """
    return boto3.client(
        service_name="s3",
        endpoint_url=s3_endpoint_url,
        aws_access_key_id=key_id,
        aws_secret_access_key=key,
        region_name='us-east-1',
        verify=False)
