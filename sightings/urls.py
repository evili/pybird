from django.conf.urls.defaults import patterns, url
from sightings.views import SightingView, IndexView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view()),
    url(r'^sighting/(?P<pk>\d+)$',
        SightingView.as_view(),
        name='sighting-detail'),
)
