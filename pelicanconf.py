# ============================================================
# 用户个人信息 - 由 scripts/apply_config.py 从 docs/ 模板生成
# 修改个人信息请编辑 docs/个人信息配置模板.md，然后运行:
#   python scripts/apply_config.py
# ============================================================
import os as _os
_site_config = _os.path.join(_os.path.dirname(__file__), 'site_config.py')
if _os.path.exists(_site_config):
    exec(compile(open(_site_config).read(), _site_config, 'exec'))

try:
    AUTHOR_LOGO = AUTHOR[0]
except NameError:
    AUTHOR_LOGO = 'B'

SITEURL = ''
SITELOGO = ''

PATH = 'content'
THEME = 'themes/custom-tailwind'
THEME_STATIC_DIR = 'theme'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DATE_FORMATS = {
    'zh': '%Y-%m-%d',
}

# Feed generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = (
    ('🏠 Home', '/'),
    ('📂 Archives', '/archives.html'),
    ('🏷️ Tags', '/tags.html'),
    ('📁 Categories', '/categories.html'),
)

# Default pagination
DEFAULT_PAGINATION = 6

# Summary
SUMMARY_MAX_LENGTH = 50

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins
PLUGINS = []

# Markdown
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {'permalink': '#'},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Static files
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
