#!/usr/bin/env python
"A basic implementation of the auth strategy abstract class"

import hashlib
from pal.authentication.auth_strategy import AbstractAuthenticationStrategy
import pal.config.configure as configure


class BasicAuthenticationStrategy(AbstractAuthenticationStrategy):
    """
    The authentication strategy to be used for dummy auth
    """
    def authenticate(self, username, password):
        """
        basic authentication:
        Looks up username in configuration map and compares password against
        associated md5.
        """

        # calculate expected md5sum
        provided_md5 = hashlib.md5(password.encode('utf8')).hexdigest()

        # read config
        configs = configure.read_config()

        # compare md5 of provided password against that mapped to the user
        if provided_md5 == configs[username]['password_md5']:
            return configs[username]["access_key_id"], configs[username]["secret_access_key"]
        else:
            # I'm really just phoning it in here
            raise Exception("Authentication failed")
