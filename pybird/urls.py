from django.conf import settings
from django.contrib.gis import admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('haystack.urls')),
    path('photos/',  include('photos.urls')),
    path('clades/',  include('clades.urls')),
    path('sightings/',  include('sightings.urls')),
    path('', 'pybird.views.index', name='home'),
]


# rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
            path('rosetta/', include('rosetta.urls')),
    ]
