from pal.requests.presigned import get_presigned_download
from pal.requests.target import SymlinkTargetSpec 


def build_symlink(s3_client, bucket_name, object_key, symlink_target_spec):
    if(__target_object_exists(s3_client, symlink_target_spec)):
        __create_symlink_object(s3_client, bucket_name, object_key, symlink_target_spec)
        return True
    return False


def __create_symlink_object(s3_client, bucket_name, object_key, target):
    target_url = get_presigned_download(s3_client, target.bucket, target.key)
    return s3_client.put_object(
        Body=str.encode(target.filepath),
        Key=object_key,
        Bucket=bucket_name,
        Metadata={
            'mode': '41344',
            'symlink': target.target
            }
        )


def __target_object_exists(s3_client, target):
    if target.bucket is None or target.key is None:
        return False
    try:
        s3_client.head_object(Bucket=target.bucket, Key=target.key)
        return True
    except:
        return False
