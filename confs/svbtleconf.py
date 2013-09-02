THEME = u'flasky' 

AUTHOR = u'Ricardo Ruiz'
SITENAME = u"RicarDotPy"
SITEURL = 'http://ricardotpy.zz.mu'
TIMEZONE = "Europe/Madrid"

#Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('Projects', 'pages/projects.html'),
        ('Talks', 'pages/talks.html'),
        ('About', 'pages/about-me.html')]

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
'en': '%d %m %Y'
}
DEFAULT_DATE_FORMAT = '%d %m %Y'

DISQUS_SITENAME = "ricardotpy"
TWITTER_USERNAME = 'riki319'
LINKEDIN_URL = 'http://es.linkedin.com/riki319'
GITHUB_URL = 'http://github.com/riki319'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 10

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = 'generado'

GOOGLE_ANALYTICS_ACCOUNT = 'UA-16479483-10'

PIWIK_URL = 'ricardotpy.zz.mu/analytics'
PIWIK_SSL_URL = 'ricardotpy.zz.my/analytics'
PIWIK_SITE_ID = '1'

MAIL_USERNAME = 'riki319'
MAIL_HOST = 'gmail.com'

# static paths will be copied under the same name
STATIC_PATHS = ["images"]

# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
