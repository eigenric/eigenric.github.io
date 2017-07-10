# Pelican Basics

THEME='pneumatic'
AUTHOR = 'Ricardo Ruiz'
SITENAME = "Pwaqø"
SITEURL = 'http://pwaqo.ml'

PATH = '../blog'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = u'es'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d de %B de %Y'

# Permalinks

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'archive'
ARCHIVES_SAVE_AS = 'archive/index.html'

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

# Pneumatic Config

BIO_TEXT = "Ceci n'est pas moi"
FA_EMBED_CODE = "d6199a8f5e"
ICONS_PATH = "images/icons"
INDEX_DESCRIPTION = "Pwaqo's blog"

DISQUS_SITENAME = "www-pwaqo-tk"
GOOGLE_ANALYTICS = "UA-16479483-12"

SOCIAL_ICONS = [
        ('http://www.github.com/pwaqo', 'GitHub', 'fa-github'),
        ('mailto:pwaqostao@gmail.com', 'Email', 'fa-envelope'),
        ('/atom.xml', 'Feed', 'fa-rss')
]

SIDEBAR_LINKS = [
        "<a href='/me/'>Acerca</a>",
        "<a href='/archive/'>Archivo</a>"
]

FOOTER_TEXT = (
     "Con <icon class='icon fa fa-heart'></icon>"
     " por Ricardo Ruiz gracias a <a href='http://www.getpelican.com'>Pelican</a>"
     " y a <a href='http://www.python.org'>Python</a><br>"
     " Obra licenciada bajo <a target='_blank'"
     " href='http://creativecommons.org/licenses/by-nc-sa/4.0/'>"
     "<img src='https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png'></a>"
)

PLUGINS = [
        'plugins.summary.summary',
        #'plugins.read_more_link.read_more_link']
        'plugins.assets.assets',
        'plugins.neighbors.neighbors',
        'plugins.sitemap.sitemap'
]

# 404.html Page

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

# Robots and extras

STATIC_PATHS = ['images', 'extra']
extras = ['CNAME', 'robots.txt']
EXTRA_PATH_METADATA = {'extra/%s' % name: {'path': name} for name in extras}

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

SUMMARY_END_MARKER = "<!-- readmore -->" # In rST .. readmore
#READ_MORE_LINK_FORMAT = "<a class='more' href='%s/{url}'>{text}</a>" % SITEURL
#READ_MORE_LINK = "[Leer más]"
