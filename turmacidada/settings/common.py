# -*- coding: utf8 -*-
"""Django common settings for turmacidada project.
See http://rdegges.com/the-perfect-django-settings-file."""

import sys
from os.path import abspath, basename, dirname, join, normpath
from os import environ

from django_cms import *

print "Executing configuration file common.py"

## The django_cms.py module defines some variables used in this module here:
## INSTALLED_APPS
## MIDDLEWARE_CLASSES
try:
	from django_cms import INSTALLED_APPS
except NameError:
	INSTALLED_APPS = []
try:
	from django_cms import MIDDLEWARE_CLASSES
except NameError:
	MIDDLEWARE_CLASSES = []
#####

########## DEBUG CONFIGURATION
# Disable debugging by default.
if environ.get('DEBUG') in ('True', '1'):
	DEBUG = True
	TEMPLATE_DEBUG = True
else:
	DEBUG = False
	TEMPLATE_DEBUG = False

# DEBUG = False
# TEMPLATE_DEBUG = True
##########

########## PATH CONFIGURATION
# Absolute filesystem path to this Django project directory.
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Site name
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)

# I'm not using this...
# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
# SECRET_FILE = normpath(join(SITE_ROOT, 'deploy', 'SECRET'))

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)
sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))
sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))
########## END PATH CONFIGURATION







# ADMIN_MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'static'))


########## MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# Absolute path to the directory static files should be collected to. Don't put
# anything in this directory yourself; store your static files in apps' static/
# subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = 'http://localhost:8000/static/'
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))

# URL prefix for static files.
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files.
STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	# normpath(join(DJANGO_ROOT, 'static')),
)

# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
INSTALLED_APPS += (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	## Admin panel and documentation. (leave this for django_cms)
	# 'django.contrib.admin',
	# 'django.contrib.admindocs',

	# 'staticfiles', # uncommenting this is giving error
	# South migration tool.
	#'south',
)

INSTALLED_APPS += (
	# Celery task queue.
	# 'djcelery',

	# django-sentry log viewer.
	# 'indexer',
	# 'paging',
	# 'sentry',
	# 'sentry.client',
)
########## END APP CONFIGURATION



########## KEY CONFIGURATION, I'm not using this
# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.
# def gen_secret_key(l):
#     """Generate a random secret key of length l."""
#     import random
#     return ''.join(choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(l))
# try:
#     SECRET_KEY = open(SECRET_FILE).read().strip()
# except IOError:
#     try:
#         with open(SECRET_FILE, 'w') as f:
#             f.write(gen_secret_key(50))
#     except IOError:
#         raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
# Make this unique, and don't share it with anybody.
SECRET_KEY = '_rcsqdgzt^edj6)#$c7tasz=*n)f54ru&amp;$a*@0kgv-j(xuybxw'
########## END KEY CONFIGURATION










# I don't know what this is for...
# Python dotted path to the WSGI application used by Dja'ngo's runserver.
WSGI_APPLICATION = 'turmacidada.wsgi.application'

########## MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = (
	('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Brazil'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
########## END GENERAL CONFIGURATION


########## TEMPLATE CONFIGURATION
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	#'django.template.loaders.eggs.Loader',
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
	normpath(join(DJANGO_ROOT, 'templates')),
)

settings_context = lambda context: custom_context
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.i18n',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'cms.context_processors.media',
	'sekizai.context_processors.sekizai',
	'turmacidada.settings.common.settings_context',
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
## already satisfied in django_cms.py
# MIDDLEWARE_CLASSES += (
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     # Uncomment the next line for simple clickjacking protection:
#     # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )
# ########## END MIDDLEWARE CONFIGURATION


########## LOGGING CONFIGURATION
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}
########## END LOGGING CONFIGURATION