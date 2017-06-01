#!/usr/bin/env python
"An implementation of the auth strategy abstract class"

import pal.authentication.auth_strategy.AbstractAuthenticationStrategy as AbstractAuthenticationStrategy


class RealAuthenticationStrategy(AbstractAuthenticationStrategy):
    """
    The authentication strategy to be used for users with real authentication credentials
    """
    def authenticate(self, username, password):
        "Real implementation of authentication"
        # TODO(andreas): implement this method
        print("hi")

