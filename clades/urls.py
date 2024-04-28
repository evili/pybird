from django.conf.urls.defaults import patterns, url
# from django.views.generic.simple import direct_to_template
# from django.conf import settings
from clades.views import IndexView, SpeciesView

urlpatterns = patterns(
        '',
        url(r'^$', IndexView.as_view()),
        url(r'^species/(?P<pk>\d+)$', SpeciesView.as_view(),
            name='species-detail'),
)
