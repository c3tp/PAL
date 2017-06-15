#!/usr/bin/env python3

import string
import boto3
import pal.config.defaults as defaults
import pal.authentication.auth_strategy as auth_strats
import pal.authentication.dummy_strategy as dummy_strategy
import pal.authentication.basic_strategy as basic_strategy


def get_dummy_client(target_endpoint):
    strategy = dummy_strategy.DummyAuthenticationStrategy()
    s3_client = get_client(strategy, "dummy_user", "dummy_password", target_endpoint)
    return s3_client

def get_basic_client(username: string, password: string, target_endpoint: string):
    strategy = basic_strategy.BasicAuthenticationStrategy()
    s3_client = get_client(strategy, username, password, target_endpoint)
    return s3_client


def get_client(
        auth_strategy: auth_strats.AbstractAuthenticationStrategy,
        username: string,
        password: string,
        target_endpoint: string):
    key_id, key = auth_strategy.authenticate(username, password)
    print("keys are %s: %s" % (key_id, key))
    return get_wos_client(
        key_id=key_id,
        key=key,
        target_endpoint=target_endpoint)


def get_wos_client(key_id, key, target_endpoint):
    return get_raw_boto_client(
        s3_endpoint_url=target_endpoint,
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
