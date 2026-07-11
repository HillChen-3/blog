# This file is only used for publishing to production
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

_siteurl = os.environ.get('SITEURL', '')
SITEURL = _siteurl if _siteurl else 'https://yourdomain.com'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Production-specific settings
GOOGLE_ANALYTICS = ''
