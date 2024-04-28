from django.contrib.gis import admin
from django.contrib import admin as django_admin

from sightings.models import Sighting,Author

admin.site.register(Sighting, admin.OSMGeoAdmin)
django_admin.site.register(Author)
