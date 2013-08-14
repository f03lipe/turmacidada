
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

from django.contrib import admin
admin.autodiscover()

import cms.urls

urlpatterns = patterns('', 
	# custom redirections
	(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
	(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt')),
	(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt')),
	(r'^blog', RedirectView.as_view(url='http://turmacidada.tumblr.com')),
	(r'^osite', TemplateView.as_view(template_name="osite.html")),
	

	# cms related
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(cms.urls)),

	# media related
	url(r'', include('django.contrib.staticfiles.urls')),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)

if 'tinymce' in settings.INSTALLED_APPS:
	urlpatterns += patterns('', (r'^tinymce/', include('tinymce.urls')))

if 'haystack' in settings.INSTALLED_APPS:
	print "Using haystack"
	import haystack.urls
	from haystack.views import SearchView

	urlpatterns += patterns('haystack.views',
		url(r'^search/?', include(haystack.urls)),
	    url(r'^$', SearchView(), name='haystack_search'),
	)

urlpatterns += staticfiles_urlpatterns()