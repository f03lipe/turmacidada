# -*- coding: utf8 -*-
"""Settings and globals for production environments.
Meant to be executed inside heroku only."""

print "Executing configuration file prod.py"

from os import environ
from sys import exc_info
from urlparse import urlparse, uses_netloc

from common import *

# Helper lambda for gracefully degrading environmental variables:
env = lambda e, d: environ[e] if environ.has_key(e) else d

import dj_database_url
DATABASES = {
	'default': dj_database_url.config(),
}

# CSRF_COOKIE_DOMAIN = '.turmacidada.org'

########## DATABASE CONFIGURATION
# See: http://devcenter.heroku.com/articles/django#postgres_database_config
uses_netloc.append('postgres')
uses_netloc.append('mysql')

try:
    if environ.has_key('DATABASE_URL'):
        url = urlparse(environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print "Unexpected error:", exc_info()

SOUTH_DATABASE_ADAPTERS = {
	'default': 'south.db.postgresql_psycopg2'
}
########## END DATABASE CONFIGURATION




########## S3 CONFIGURATION
# We use S3 as our media backend on Heroku, so set that up
AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = environ['S3_BUCKET_NAME']
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# DEFAULT_FILE_STORAGE = 'turmacidada.settings.storage.CachedS3BotoStorage'

MEDIASYNC = {
	'BACKEND': 'mediasync.backends.s3',
    'AWS_KEY': AWS_ACCESS_KEY_ID,
    'AWS_SECRET': AWS_SECRET_ACCESS_KEY,
    'AWS_BUCKET': AWS_STORAGE_BUCKET_NAME,
	
    # 'SERVE_REMOTE': True,
	'AWS_BUCKET_CNAME': True,
	'DOCTYPE': 'html4',
	'USE_SSL': False,
	'CACHE_BUSTER': 1234,
}

# Adjust media URL to point directly to S3
MEDIA_URL = 'http://turmacidada-bucket.s3.amazonaws.com/'
# STATIC_URL = 'http://turmacidada.herokuapp.com/static/' # normpath(join(DJANGO_ROOT, 'static'))

# Adjust thumbnail storage
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
########## END S3 CONFIGURATION






######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', 'smtp.gmail.com')
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', '')
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', 'your_email@example.com')
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-port
EMAIL_PORT = env('EMAIL_PORT', 587)
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#email-use-tls
EMAIL_USE_TLS = True
# See: https://docs.djangoproject.com/en/1.3/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION









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
## https://github.com/atodorov/django-s3-cache
# CACHES = {
#     'default': {
#         'BACKEND': 's3cache.AmazonS3Cache',
#         'OPTIONS': {
#             'ACCESS_KEY_ID': AWS_ACCESS_KEY_ID,
#             'SECRET_ACCESS_KEY': AWS_SECRET_ACCESS_KEY,
#             'STORAGE_BUCKET_NAME': AWS_STORAGE_BUCKET_NAME,
#             'REDUCED_REDUNDANCY': True
#         }
#     }
# }
########## END CACHE CONFIGURATION
