# This file is only used for publishing to production
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://hillchen-3.github.io/blog'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Production-specific settings
GOOGLE_ANALYTICS = ''
