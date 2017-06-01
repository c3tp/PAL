# PAL
Platform Access Layer. 

Requires a config file defined at /etc/pal.conf in yaml format. 

must contain: 
- "access_key_id"
- "secret_access_key"
yaml keys. 

## Install guide

Install python3, and pip. 

Run: 
```
python setup.py install
pal
```

Above command just runs default action against WOS deployment with default token_id/token stored in config file. 