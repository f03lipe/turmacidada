
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import haystack.urls
import cms.urls

urlpatterns = patterns('', 
	# custom redirections
	(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
	(r'^robots\.txt$', 'django.views.generic.simple.redirect_to', {'url': '/static/robots.txt'}),
	(r'^blog', 'django.views.generic.simple.redirect_to', {'url': 'http://turmacidada.tumblr.com'}),

	# cms related
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/?', include(haystack.urls)),
	url(r'^', include(cms.urls)),

#	(r'^tinymce/', include('tinymce.urls')),

	# media related
	url(r'', include('django.contrib.staticfiles.urls')),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
	url(r'^', include('mediasync.urls')),
)

from haystack.views import SearchView

urlpatterns += patterns('haystack.views',
    url(r'^$', SearchView(), name='haystack_search'),
)

# urlpatterns += staticfiles_urlpatterns()