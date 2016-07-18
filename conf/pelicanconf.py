#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


# Pelican Basics

THEME='pupil'
AUTHOR = 'Ricardo Ruiz'
SITENAME = "Pwaqø"
SITEURL = ['http://localhost:8000', 'http://192.168.1.131:8000'][0]

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
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'
ARCHIVES_URL = 'archivo'
ARCHIVES_SAVE_AS = 'archivo/index.html'


# Feed

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Iris Config

GOOGLE_FONTS = ['Ribeye Marrow']

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('Archivo',ARCHIVES_URL),
             ('Tags', TAGS_URL),)

USER_LOGO = 'perfil.jpg'

SOCIAL = (('github', 'http://www.github.com/pwaqo'),
          ('twitter', 'http://www.twitter.com/pwaqostao'),)

EMAIL = 'pwaqostao@gmail.com'


'''OTHERS = ['Flavors', 'Fascinate', 'Lakki Reddy', 'Open Sans', 
	  'Playfair Display', 'Vollkorn', 'Ribeye Marrow', 
  	   'Oleo Script Swash Caps', 'Lobster']'''

# Plugins

PLUGINS = ['plugins.summary.summary', 'plugins.read_more_link.read_more_link']

SUMMARY_END_MARKER = "<!-- readmore -->" # In rST .. readmore
READ_MORE_LINK_FORMAT = "<a class='more' href='%s/{url}'>{text}</a>" % SITEURL
READ_MORE_LINK = '[Leer más]'
