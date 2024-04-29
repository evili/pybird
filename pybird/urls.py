from django.conf import settings
from django.contrib.gis import admin
from django.contrib import admin
from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photos/',  include('photos.urls')),
    path('clades/',  include('clades.urls')),
    path('sightings/',  include('sightings.urls')),
    path('', IndexView.as_view(), name='home'),
]

# haystack
if 'haystack' in settings.INSTALLED_APPS:
    urlpatterns += [ path('search/', include('haystack.urls')), ]

# rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
            path('rosetta/', include('rosetta.urls')),
    ]
