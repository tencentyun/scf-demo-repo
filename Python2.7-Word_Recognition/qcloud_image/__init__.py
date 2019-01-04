# -*- coding: utf-8 -*-

__version__ = '1.0.0'

from .auth import Auth
from .api  import Client
from .type import *

import logging

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
