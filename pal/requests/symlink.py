from pal.requests.presigned import get_presigned_download


def build_symlink(s3_client, bucket_name, object_key, target):
    if(__target_object_exists(s3_client, target)):
        __create_symlink_object(s3_client, bucket_name, object_key, target)
        return True
    return False


def __parse_key_bucket(target):
    return target.split('/', 1)


def __create_symlink_object(s3_client, bucket_name, object_key, target):
    target_bucket, target_key = __parse_key_bucket(target)
    target_url = get_presigned_download(s3_client, target_bucket, target_key)
    return s3_client.put_object(
        Body=str.encode(target_url),
        Key=object_key,
        Bucket=bucket_name,
        Metadata={
            'symlink': target
            }
        )


def __target_object_exists(s3_client, target):
    target_bucket, target_key = __parse_key_bucket(target)
    if target_bucket is None or target_key is None:
        return False
    try:
        s3_client.head_object(Bucket=target_bucket, Key=target_key)
        return True
    except:
        return False
