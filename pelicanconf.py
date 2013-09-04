from __future__ import unicode_literals

THEME = 'flasky' 

# Site 

AUTHOR = 'Ricardo Ruiz'
SITENAME = "Ricardo.Py"

TIMEZONE = "Europe/Madrid"

DEFAULT_CATEGORY = '/dev/random'
DEFAULT_DATE_FORMAT = '%a %d %b %Y'
DEFAULT_DATE = 'fs' # Hora generada automaticamente

STATIC_PATHS = ["images", "pdfs"]



SECTIONS = [('Blog', 'index.html'),
        ('Archivo', 'archives.html'),
        ('Tags', 'tags.html'),
        ('About me', 'pages/about-me.html')]

# Theme

DISQUS_SITENAME = "ricardotpy"
TWITTER_USERNAME = 'riki319'
GITHUB_URL = 'http://github.com/riki319/ricardotpy'
FACEBOOK = True
GOOGLE_ANALYTICS = 'UA-16479483-10'


EMAIL = 'riki319@gmail.com'

SOCIAL = (('github', 'http://github.com/riki319'),
		  ('twitter', 'http://twitter.com/riki319'),
		  ('facebook', 'http://facebook.com/riki319'))

LINKS = (('Geekia', 'http://geekia.es'),)


REVERSE_CATEGORY_ORDER = False
DEFAULT_PAGINATION = 5

# Feed

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Plugins

PLUGIN_PATH = 'plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar']

FILES_TO_COPY = (('extra/.htaccess', '.htaccess'),
				('extra/google53aa3b50d6efd909.html', 'google53aa3b50d6efd909.html'))
