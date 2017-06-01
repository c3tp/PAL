#!/usr/bin/env python
"An abstract base class for authentication strategies"

from abc import ABC, abstractmethod


class AbstractAuthenticationStrategy(ABC):
    """
    Abstract base class for different authentication strategies.
    Authentication strategies are for getting s3 auth tokens/names.
    """
    def __init(self):
        "Initialization method"
        super(AbstractAuthenticationStrategy, self).__init__()

    @abstractmethod
    def authenticate(self, username, password):
        "Abstract class for getting s3 auth tokens/names from uname/passwd"
        pass
