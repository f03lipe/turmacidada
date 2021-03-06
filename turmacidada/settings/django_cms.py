# -*- coding: utf8 -*- 
"""Settings and globals django-cms related."""

print "Executing configuration file django_cms.py"

from os import environ

# Helper lambda for gracefully degrading environmental variables:
env = lambda e, d: environ[e] if environ.has_key(e) else d

# basic django-cms only
# DON'T ADD ANYTHING HERE!
INSTALLED_APPS = (
	'cms',
	'mptt',
#	'reversion',
	'south',
	'appmedia',
	'menus',
	
	# Dependencies (or installed alongside)
	'sekizai',		# for template functionallity: "addtoblock" etc
)

# admin interface related apps
INSTALLED_APPS += (
	'django.contrib.admin',
	'django.contrib.admindocs',
)

# application related apps
INSTALLED_APPS += (
	'turmacidada',				# the project
	'turmacidada.website',		# the project's app
)

INSTALLED_APPS += (
	'easy_thumbnails',
	'filer',
	
	'cms.plugins.file',
	'cms.plugins.flash',
	'cms.plugins.googlemap',
	'cms.plugins.link',
	'cms.plugins.picture',
	'cms.plugins.snippet',
	'cms.plugins.teaser',
	'cms.plugins.text',
	'cms.plugins.video',
	'cms.plugins.twitter',
)

# storage related
INSTALLED_APPS += (
 	'storages',
	'memcache',
	'haystack', 	# to search
	'tinymce',		
#	'compressor', 	# to compress files
	'boto',
# 	's3cache',

# # filer plugin
#  	'cmsplugin_filer_file',
#  	'cmsplugin_filer_folder',
#  	'cmsplugin_filer_image',
#  	'cmsplugin_filer_teaser',
#  	'cmsplugin_filer_video',
)

FOOTER_LINKS = {
	'sobre o site': '/osite',
	'imprensa': '/imprensa',
#	'núcleos': '/nucleos',
	'blog': 'http://turmacidadabrasil.tumblr.com'
}

########## HTML MINIFY CONFIGURATION
HTML_MINIFY = True
########## END HTML MINIFY CONFIGURATION

########## HAYSTACK CONFIGURATION
from os.path import join, dirname, abspath

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
		'PATH': join(DJANGO_ROOT, 'whoosh_index'),
	},
}
HAYSTACK_WHOOSH_PATH = join(DJANGO_ROOT, 'whoosh_index')
########## END HAYSTACK CONFIGURATION

# djang-cms installation process
MIDDLEWARE_CLASSES = (
    'htmlmin.middleware.HtmlMinifyMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
)

THUMBNAIL_PROCESSORS = (
	'easy_thumbnails.processors.colorspace',
	'easy_thumbnails.processors.autocrop',
	'easy_thumbnails.processors.scale_and_crop',
	'filer.thumbnail_processors.scale_and_crop_with_subject_location',
	'easy_thumbnails.processors.filters',
)

# djang-cms installation process
gettext = lambda s: s

LANGUAGES = [
	('pt', gettext('Portuguese')),
#	('en', gettext('English')),
#	('de', gettext('German')),
#	('fe', gettext('French')),
]
CMS_HIDE_UNTRANSLATED = False
CMS_FRONTEND_LANGUAGES = (
	'pt', 'en'
)

CMS_LANGUAGES = {
	1: [
		{'code': 'pt',	'name': gettext('Portuguese')},
		{'code': 'en',	'name': gettext('English')},
		# {'code': 'de', 	'name': gettext('Deutsch')},
		# {'code': 'fr', 	'name': gettext('French')},
	],
	'default': {
		'fallbacks': ['pt'],
		'redirect_on_fallback': False,
		'public': True,
		'hide_untranslated': False,
	}
}



CMS_TEMPLATES = (
	# ('pages/404.html', '404 page'),
	('base.html', 'Base Template'),
		('pages/home.html', 'Home Page'),
		('pages/about.html', 'About'),
		('pages/projects.html', 'Projects'),
		('pages/team.html', 'Team'),
		('pages/blank.html', 'Blank'),
		('pages/contact.html', 'Contact'),
)

import datetime

BLOG_URL = 'http://turmacidadabrasil.tumblr.com'

########## CUSTOM CONTEXT
custom_context = {
	'address': 'Rua Gal. Canabarro, 552, sala 3, Campus 3. Maracanã, Rio de Janeiro ',
	'tel': '(021) 2566 3055',
	'email': 'turmacidadabrasil@gmail.com',
	'sn': {
		'facebook': 'http://facebook.com/turmacidadabrasil',
		'twitter': 'http://twitter.com/turmacidada',
#		'vimeo': 'http://vimeo.com',
		'google-plus': 'http://+.google.com',
		'flickr': 'http://www.flickr.com/photos/turmacidada',
		'rss': 'http://turmacidadabrasil.tumblr.com/rss',
	},
	'blog_url': BLOG_URL,
	'FOOTER_LINKS': FOOTER_LINKS,
	'TODAY': datetime.date.today(),
	'UNDER_CONSTRUCTION': environ.get('UNDER_CONSTRUCTION') == 'True'
}
########## END CUSTOM CONTEXT


