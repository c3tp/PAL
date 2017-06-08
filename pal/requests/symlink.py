from pal.requests.presigned import get_presigned_download


def build_symlink(s3_client, bucket_name, object_key, target_bucket, target_key):
    if(__target_object_exists(s3_client, target_bucket, target_key)):
        __create_symlink_object(s3_client, bucket_name, object_key, target_bucket, target_key)
        return True
    return False


def __create_symlink_object(s3_client, bucket_name, object_key, target_bucket, target_key):
    target_url = get_presigned_download(s3_client, bucket_name, object_key)
    return s3_client.put_object(
            Body=str.encode(target_url),
            Key=object_key,
            Bucket=bucket_name,
            Metadata={
                'symlink': target_bucket.join(target_key)
            }
        )


def __target_object_exists(s3_client, target_bucket, target_key):
    try:
        s3_client.head_object(Bucket=target_bucket, Key=target_key)
        return True
    except:
        return False
