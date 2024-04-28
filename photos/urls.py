from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template

urlpatterns = patterns(
        '',
        (r'^$', 'django.views.generic.simple.direct_to_template',
         {
             'template': 'photos/index.html',
             'menu': ['Add', 'Search', 'Equipment']}),
        (r'^equipment/', direct_to_template,
         {
            'template': 'photos/equipment.html'}),
        (r'^kml/', 'photos.views.all_kml'),
        (r'^detail/(?P<id>\d+)$', 'photos.views.detail')
)
