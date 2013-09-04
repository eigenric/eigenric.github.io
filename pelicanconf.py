from __future__ import unicode_literals

THEME = 'notmyidea' 

AUTHOR = 'Ricardo Ruiz'
SITENAME = "RicarDotPy"
SITEURL = 'http://www.ricardotpy.tk/'
TIMEZONE = "Europe/Madrid"

DEFAULT_CATEGORY = '/dev/random'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d %Y'



AUTHOR_BIO = "Geek & Pythonista"



LINKS = (
			('Twitter', 'http://twitter.com/riki319'),
			('Github', 'http://github.com/riki319')
		)


DISQUS_SITENAME = "ricardotpy"
TWITTER_USERNAME = 'riki319'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 10

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

GOOGLE_ANALYTICS = 'UA-16479483-10'


# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/.htaccess', '.htaccess'),)
