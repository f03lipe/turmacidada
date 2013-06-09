# -*- coding: utf8 -*-
"""Settings and globals for development environments."""

print "Executing configuration file dev.py"

from common import *

from os.path import join, normpath

from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

########## EMAIL CONFIGURATION
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
########## END EMAIL CONFIGURATION

DEBUG = True

########## DATABASE CONFIGURATION
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': normpath(join(SITE_ROOT, 'database.sqlite')),
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}

########## END DATABASE CONFIGURATION


########## S3 CONFIGURATION (uncomment to use S3 locally)
# We use S3 as our media backend on Heroku, so set that up
# Import S3 keys.
from keys import * 
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# DEFAULT_FILE_STORAGE = 'turmacidada.settings.storage.CachedS3BotoStorage'

# Adjust thumbnail storage
THUMBNAIL_DEFAULT_STORAGE = '' # DEFAULT_FILE_STORAGE
########## END S3 CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
	}
}
########## END CACHE CONFIGURATION


########## DJANGO-DEBUG-TOOLBAR CONFIGURATION
# MIDDLEWARE_CLASSES += (
# 	'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# INSTALLED_APPS += (
# 	'debug_toolbar',
# )

# IPs allowed to see django-debug-toolbar output.
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
	# If set to True (default), the debug toolbar will show an intermediate
	# page upon redirect so you can view any debug information prior to
	# redirecting. This page will provide a link to the redirect destination
	# you can follow when ready. If set to False, redirects will proceed as
	# normal.
	'INTERCEPT_REDIRECTS': False,

	# If not set or set to None, the debug_toolbar middleware will use its
	# built-in show_toolbar method for determining whether the toolbar should
	# show or not. The default checks are that DEBUG must be set to True and
	# the IP of the request must be in INTERNAL_IPS. You can provide your own
	# method for displaying the toolbar which contains your custom logic. This
	# method should return True or False.
	'SHOW_TOOLBAR_CALLBACK': None,

	# An array of custom signals that might be in your project, defined as the
	# python path to the signal.
	'EXTRA_SIGNALS': [],

	# If set to True (the default) then code in Django itself won't be shown in
	# SQL stacktraces.
	'HIDE_DJANGO_SQL': True,

	# If set to True (the default) then a template's context will be included
	# with it in the Template debug panel. Turning this off is useful when you
	# have large template contexts, or you have template contexts with lazy
	# datastructures that you don't want to be evaluated.
	'SHOW_TEMPLATE_CONTEXT': True,

	# If set, this will be the tag to which debug_toolbar will attach the debug
	# toolbar. Defaults to 'body'.
	'TAG': 'body',
}
########## END DJANGO-DEBUG-TOOLBAR CONFIGURATION


########## CELERY CONFIGURATION
# INSTALLED_APPS += (
# 	'djkombu',
# )
# 
# BROKER_BACKEND = 'djkombu.transport.DatabaseTransport'
########## END CELERY CONFIGURATION

########## CACHE CONFIGURATION
## See: https://docs.djangoproject.com/en/1.3/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'localhost:11211',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'ketama': True,
        }
    }
}
############



###################

# import os

# PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# # Absolute filesystem path to the directory that will hold user-uploaded files.
# # Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = join(DJANGO_ROOT, "media")

# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash.
# # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# # Absolute path to the directory static files should be collected to.
# # Don't put anything in this directory yourself; store your static files
# # in apps' "static/" subdirectories and in STATICFILES_DIRS.
# # Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

# # URL prefix for static files.
# # Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'

# # Additional locations of static files
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )

# # List of finder classes that know how to find static files in
# # various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )