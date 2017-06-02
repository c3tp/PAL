#!/usr/bin/env python
"""Create API For presigned URLS to objects"""

import boto3
import pal.requests.client


def get_presigned_download(s3_client, bucket_name, object_key):
    return s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': object_key
        })


def get_presigned_upload(s3_client, bucket_name, object_key):
    # TODO(Andreas):
    return s3_client.generate_presigned_post(
        Bucket=bucket_name,
        Key=object_key
    )

