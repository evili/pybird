from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.gis import admin


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybird.views.home', name='home'),
    # url(r'^pybird/', include('pybird.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^search/', include('haystack.urls')),
    (r'^photos/',  include('photos.urls')),
    (r'^clades/',  include('clades.urls')),
    (r'^sightings/',  include('sightings.urls')),
    (r'^$', 'pybird.views.index'),
)

# rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
            '',
            url(r'^rosetta/', include('rosetta.urls')),
    )

# Media Files in Debug Mode
if settings.DEBUG:
    _media_url = settings.MEDIA_URL

    urlpatterns += patterns(
            '',
            (r'^%s(?P<path>.*)$' % _media_url,
             'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
