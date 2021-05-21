"""
===================
betteraiohttp
===================

A better version of aiohttp that allows for url filtering and rickroll detection.

|Status badge| |Docs badge| |Downloads badge|

.. |Status badge| image:: https://github.com/BobDotCom/betteraiohttp/workflows/Python%20Package/badge.svg
   :target: https://github.com/BobDotCom/betteraiohttp/actions?query=workflow%3A"Python+Package"
   :alt: Package Status

.. |Docs badge| image:: https://readthedocs.org/projects/betteraiohttp/badge/?version=latest
   :target: https://betteraiohttp.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |Downloads badge| image:: https://static.pepy.tech/personalized-badge/betteraiohttp?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
   :target: https://pepy.tech/project/betteraiohttp
   :alt: Download Counter

PyPI: https://pypi.org/project/betteraiohttp/

Docs: https://betteraiohttp.readthedocs.io/en/latest/

Installation
############
You can install released versions of growstocks from the Python Package Index via pip or a similar tool:

**Stable Release:** ``pip install betteraiohttp``

**Working Version:** ``pip install git+https://github.com/BobDotCom/betteraiohttp.git``

Usage
#####
Used in the exact same way as aiohttp, except the response object has blocked and rickroll attributes.
"""

from . import errors
from .client import *

# PACKAGE INFO
__title__ = "betteraiohttp"
__author__ = 'BobDotCom'
__version__ = '0.1.0'

__license__ = "MIT License"
__copyright__ = "Copyright 2021 {}".format(__author__)
