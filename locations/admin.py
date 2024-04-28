from django.contrib.gis import admin
from locations.models import Zone

admin.site.register(Zone, admin.OSMGeoAdmin)
