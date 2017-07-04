# PAL
Platform Access Layer. 

Requires a config file defined at `/etc/pal.conf` in YAML format which must define for basic authentication a user, keyed on their username, with attributes `password_md5`, `access_key_id` and `secret_access_key` for S3 access.  For example:

```
routing_endpoint: some_url_to_an_s3_endpoint. 
Frances:
  password_md5: b63a52d38855ad89a14ff3c42f19d209
  access_key_id: ABCDEF123456XYZSS3I
  secret_access_key: Qu3Bl33pBl0rpad1ngd0ng+w1ngnutsRuSS/wrtM
```

## Basic Install Guide

This supposes you're running minio at localhost:9000. if not,
go to `./pal/config/defaults.py` and modify the target url to wherever you want it to go. 

```
routing_endpoint: https://s3-uvic.dev.computecanada.ca
```

(In our case for WOS, we'd be switching this to the wos IP)

### Run via docker

Add a file at the root directory of this project named `pal.conf` with the above specification.

Run:
```
docker build . -t c3tp/pal
docker run --net=host -p 5000:5000 c3tp/pal
```

You now have PAL running. 

### Manual Install

Install python3, virtualenv, and pip.

```
git clone https://github.com/c3tp/PAL
cd pal
virtualenv env -p /usr/bin/python3
source env/bin/activate
```

Run: 
```
python setup.py install
palw
```

The above command just runs default action against WOS deployment with default token_id/token stored in config file
in `pal.conf`.

## Possible commands

Do

```
echo "127.0.0.1 localsite" > /etc/hosts
```

make curl requests such as 
```
curl -XPOST localsite:5000/peter/test.log/presigned_url -d "username=haha&password=yup&dummy=True  "
curl -XPOST localsite:5000/peter/test.log/presigned_post -d "username=haha&password=yup&dummy=True"
curl -XPOST localsite:5000/peter/vis/symlink -d "username=haha&password=yup&target=peter/test.log&dummy=True"
```

A better alternative is to use the PAL client and library.

