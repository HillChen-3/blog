AUTHOR = 'Your Name'
AUTHOR_LOGO = 'Y'
SITENAME = 'Your Blog Name'
SITEDESCRIPTION = 'A personal blog about coding, technology, and learning notes.'
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

# Social links (Font Awesome icon names)
SOCIAL = (
    ('github', 'https://github.com/'),
    ('twitter', 'https://twitter.com/'),
    ('linkedin', 'https://linkedin.com/in/'),
)

# Homepage settings
ABOUT_ME = '''I'm a passionate software developer who loves exploring new technologies and sharing knowledge through writing.

This blog is where I document my learning journey, share technical tutorials, and record my experiences with various frameworks and tools.

When I'm not coding, you can find me reading tech books, contributing to open source, or experimenting with new side projects.'''

TECH_STACK = ('Python', 'JavaScript', 'TypeScript', 'React', 'FastAPI', 'Django', 'Tailwind CSS', 'Docker', 'PostgreSQL', 'Git', 'Linux')

COPYRIGHT_YEAR = '2025'

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
