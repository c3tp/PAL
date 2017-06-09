# PAL
Platform Access Layer. 

Requires a config file defined at /etc/pal.conf in yaml format. 

must contain: 
- "access_key_id"
- "secret_access_key"
yaml keys. 

## Install guide

Install python3, virtualenv, and pip.

```
git clone https://github.com/c3tp/PAL
cd pal
virtualenv env -p /usr/bin/python3
source env/bin/activate
echo "127.0.0.1 localsite" > /etc/hosts
```

Run: 
```
python setup.py install
palw
```

make curl requests such as 
```
curl -XPOST localsite:5000/peter/test.log/presigned_url -d "username=haha&password=yup"
curl -XPOST localsite:5000/peter/test.log/presigned_post -d "username=haha&password=yup"
curl -XPOST localsite:5000/peter/vis/symlink -d "username=haha&password=yup&target=peter/test.log"
```


Above command just runs default action against WOS deployment with default token_id/token stored in config file
in /etc/pal.conf