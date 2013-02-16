# -*- coding: utf8 -*- 
"""Settings and globals django-cms related."""

print "Executing configuration file django_cms.py"

# basic django-cms only
INSTALLED_APPS = (
	'cms',
	'mptt',
	'menus',
	'sekizai',
	'cms.plugins.file',
	'cms.plugins.flash',
	'cms.plugins.googlemap',
#	'cms.plugins.link',
	'cms.plugins.picture',
	'cms.plugins.snippet',
	'cms.plugins.teaser',
	'cms.plugins.text',
	'cms.plugins.video',
	'cms.plugins.twitter',
	'django_cleanup',
)

# storage related
INSTALLED_APPS += (
	'mediasync',
	'storages',
#	'memcache',
	'boto',
#	'compressor',
#	's3cache',
)

# application related apps
INSTALLED_APPS += (
	'turmacidada',
	'turmacidada.website',
	'haystack',
	'filer',
#	'tinymce',
	'easy_thumbnails',
)

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

# filer plugin
INSTALLED_APPS += (
	'cmsplugin_filer_file',
	'cmsplugin_filer_folder',
	'cmsplugin_filer_image',
	'cmsplugin_filer_teaser',
	'cmsplugin_filer_video',
)

# djang-cms installation process
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# djang-cms installation process
gettext = lambda s: s
CMS_LANGUAGES = LANGUAGES = [
	('pt', gettext('Portuguese')),
	('en', gettext('English')),
#	('de', gettext('German')),
]

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


