# Pelican Basics

THEME = 'pneumatic'
AUTHOR = 'Ricardo Ruiz Fernández de Alba'
SITENAME = "eigenℝic"
SITEURL = 'https://localhost:8000'

PATH = 'blog'
OUTPUT_PATH = '.output'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = u'es'
# DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%-d %b %Y'

# Permalinks

RELATIVE_URLS = True

INDEX_URL = 'blog'
INDEX_SAVE_AS = 'blog.html'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'

#ARTICLE_URL = '{slug}/'
#ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

ARCHIVES_URL = 'archive'
ARCHIVES_SAVE_AS = 'archive/index.html'

YEAR_ARCHIVE_URL = 'blog/{date:%Y}'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = 'blog/{date:%Y}/{date:%m}'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags

DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''

# Disable feed except atom.xml

FEED_ATOM = 'atom.xml'
FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pneumatic theme

BIO_TEXT = "Mathematician & <br>Computer Scientist"
BIO_TEXT_MOB = "Maths & Computer Science"
SITE_AUTHOR = AUTHOR
FA_EMBED_CODE = "a4053f556f"
ICONS_PATH = "images/icons"
INDEX_DESCRIPTION = "Personal blog of Ricardo Ruiz"
THEME_COLOR = "#1e2327"

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

SOCIAL_ICONS = [
        ('http://www.github.com/eigenric', 'GitHub', 'fa-github'),
        ('http://stackoverflow.com/u/8401085', 'SO', 'fa-stack-overflow'),
        ('https://www.linkedin.com/in/ricardo-ruiz-fern%C3%A1ndez-de-alba-617253147/', 'Linkedin', 'fa-linkedin'),
        ('http://twitter.com/eigenric', 'Twitter', 'fa-twitter'),
        ('mailto:ricardoruizfdez@gmail.com', 'Email', 'fa-envelope'),
        ('/atom.xml', 'Feed', 'fa-rss')
]

SIDEBAR_LINKS = [
        ("", "Home"),
        ("blog", "Blog"),
        ("archive", "Archive")
]

FOOTER_TEXT = (
    "© 2025 por Ricardo Ruiz con"
    " <i class='icon fa fa-heart' aria-hidden='true'></i> "
)

PLUGINS = [
        'plugins.summary.summary',
        'plugins.assets.assets',
        'plugins.neighbors.neighbors',
        'plugins.sitemap.sitemap',
        'plugins.pelican_youtube',
        'pelican_katex',
        'pelican_toggle'
]

MATH_JAX = {
        # 'auto_insert': False,
        # 'mathjax_font': 'typewriter't python programmers
}

# 404.html Page

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

# Google fonts

# GOOGLE_FONTS = ['Merriweather:ital,wght@0,400;0,700;1,400']
# GOOGLE_FONTS = ['Roboto Slab:wght@400;600']
GOOGLE_FONTS = [
    "Nunito Sans:300,700",
    "Source Code Pro",
]

# Robots and extras

STATIC_PATHS = ['images', 'extra']
extras = ['CNAME', 'robots.txt', 'google6275c7be0bd2f1e6.html']
EXTRA_PATH_METADATA = {'extra/%s' % name: {'path': name} for name in extras}

ARTICLE_EXCLUDES = ['extra']
PAGE_EXCLUDES = ['extra']   

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': ['tag', 'category', 'author', 'tags', 'categories']
}

SUMMARY_MAX_LENGTH = 30
# SUMMARY_END_SUFFIX= "<a class='more' href=f'{SITEURL}/{url}'>Leer Más</a>"
# SUMMARY_END_MARKER = "<!-- readmore -->"  # In rST .. readmore
# READ_MORE_LINK_FORMAT = "<a class='more' href=%s/{url}'>{text} RE</a>" % SITEURL