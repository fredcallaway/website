#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Fred Callaway'
SITEURL = 'http://localhost:8000'
SITENAME = AUTHOR
SITETITLE = AUTHOR
SITESUBTITLE = ''
SITEDESCRIPTION = '%s\'s personal website' % AUTHOR
SITELOGO = '/images/fred-head.png'
#FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
# PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = 'flex-theme'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False

LINKS = (
)

SOCIAL = (
    ('github', 'https://github.com/fredcallaway'),
    ('paper-plane', 'mailto:fredcallaway@berkeley.edu'),
)


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

#CC_LICENSE = {
#    'name': 'Creative Commons Attribution-ShareAlike',
#    'version': '4.0',
#    'slug': 'by-sa'
#}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10
STATUSCAKE = False

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./pelican-plugins', './plugins']
PLUGINS = [
    'sitemap',
    'ipynb.markup',
    #'post_stats',
]

IPYNB_USE_METACELL = True
IPYNB_NB_OUTPUT = True
IGNORE_FILES = ['.ipynb_checkpoints']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "fredcallaway"
#ADD_THIS_ID = 'ra-55adbb025d4f7e55'


STATIC_PATHS = [
    'images',
    'charts',
    'pdfs',
    'misc',
    # 'notebooks'
    # 'blog/notebooks'
    
]

#EXTRA_PATH_METADATA = {
#    'extra/custom.css': {'path': 'static/custom.css'},
#}

# CUSTOM_CSS = 'static/custom.css'
#

USE_LESS = True