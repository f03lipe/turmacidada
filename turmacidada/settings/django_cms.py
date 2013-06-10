# -*- coding: utf8 -*- 
"""Settings and globals django-cms related."""

print "Executing configuration file django_cms.py"

# basic django-cms only
# DON'T ADD ANYTHING HERE!
INSTALLED_APPS = (
	'cms',
	'mptt',
#	'reversion',
#	'south', 	# already added
#	'appmedia',
#	'menus',
)

# admin interface related apps
INSTALLED_APPS += (
#	'django-menus',
	'haystack',					# for search
	'django.contrib.admin',
	'django.contrib.admindocs',
)

# application related apps
INSTALLED_APPS += (
	'turmacidada',				# the project
	'turmacidada.website',		# the project's app
#	'filer',
#	'tinymce',
	# 'easy_thumbnails',
)

INSTALLED_APPS += (
	'sekizai',					# for template functionallity: "addtoblock" etc
	# 'django_cleanup',
	# 'cms.plugins.file',
	# 'cms.plugins.flash',
	# 'cms.plugins.googlemap',
	# 'cms.plugins.link',
	# 'cms.plugins.picture',
	# 'cms.plugins.snippet',
	# 'cms.plugins.teaser',
	# 'cms.plugins.text',
	# 'cms.plugins.video',
	# 'cms.plugins.twitter',
)

# storage related
INSTALLED_APPS += (
# 	'storages',
# #	'memcache',
# #	'boto',
# #	'compressor',
# 	's3cache',
)

"""
# basic django-cms only
# DON'T ADD ANYTHING HERE!
INSTALLED_APPS = (
	'cms',
#	'mptt',
	'reversion',
#	'south', 	# already added
	'appmedia',
	'menus',
)

# admin interface related apps
INSTALLED_APPS += (
#	'django-menus',
	'haystack',					# for search
	'django.contrib.admin',
	'django.contrib.admindocs',
)

# application related apps
INSTALLED_APPS += (
	'turmacidada',				# the project
	'turmacidada.website',		# the project's app
#	'filer',
#	'tinymce',
	'easy_thumbnails',
)

INSTALLED_APPS += (
	'sekizai',					# for template functionallity: "addtoblock" etc
	'django_cleanup',
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
#	'memcache',
#	'boto',
#	'compressor',
	's3cache',
)
"""

# filer plugin
# INSTALLED_APPS += (
# 	'cmsplugin_filer_file',
# 	'cmsplugin_filer_folder',
# 	'cmsplugin_filer_image',
# 	'cmsplugin_filer_teaser',
# 	'cmsplugin_filer_video',
# )

########## HAYSTACK CONFIGURATION
from os.path import join, dirname, abspath

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
		'PATH': join(DJANGO_ROOT, 'whoosh_index'),
	},
}
########## END HAYSTACK CONFIGURATION

# djang-cms installation process
MIDDLEWARE_CLASSES = (
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
	('en', gettext('English')),
#	('de', gettext('German')),
#	('fe', gettext('French')),
]
CMS_HIDE_UNTRANSLATED = False
CMS_FRONTEND_LANGUAGES = ('pt', 'en')

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
		('pages/contact.html', 'Contact'),
)

########## CUSTOM CONTEXT
custom_context = {
	'sn': {
		'facebook': 'http://facebook.com',
		'twitter': 'http://twitter.com',
		'vimeo': 'http://vimeo.com',
		'flickr': 'http://flickr.com',
		'rss': 'http://turmacidada.tumblr.com/rss',
		'blog': 'http://turmacidada.tumblr.com'
	},
}
########## END CUSTOM CONTEXT


