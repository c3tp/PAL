#!/usr/bin/env python
"A dummy implementation of the auth strategy abstract class"

from pal.authentication.auth_strategy import AbstractAuthenticationStrategy
import pal.config.configure as configure


class DummyAuthenticationStrategy(AbstractAuthenticationStrategy):
    """
    The authentication strategy to be used for dummy auth
    """
    def authenticate(self, username, password):
        """
        dummy authentication:
        Ignores whatever input username/password being passed.
        Uses already known authenticated username/password to log in.
        """
        configs = configure.read_config()
        return configs["access_key_id"], configs["secret_access_key"]


