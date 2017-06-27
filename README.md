# PAL
Platform Access Layer. 

Requires a config file defined at /etc/pal.conf in yaml format. 


must contain: 
- "access_key_id"
- "secret_access_key"
- "routing_endpoint"
yaml keys for your s3 access. 

i.e.

```
access_key_id: your access key id. 
secret_access_key: your secret access key. 
routing_endpoint: http://127.0.0.1:9000

```

## Basic Install Guide

This supposes you're running minio at localhost:9000. if not,
go to `./pal/config/defaults.py` and modify the target url to wherever you want it to go. 

```
routing_endpoint: https://s3-uvic.dev.computecanada.ca
```

(In our case for WOS, we'd be switching this to the wos IP)

### Run via docker

Add a file at the root directory of this project named `pal.conf`
with the above specification.

Run
```
docker build . -t c3tp/pal
docker run c3tp/pal --net=host -p 5000:5000
```

You now have pal running. 


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




Above command just runs default action against WOS deployment with default token_id/token stored in config file
in /etc/pal.conf


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
