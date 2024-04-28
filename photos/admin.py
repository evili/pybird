from django.contrib.gis import admin
from photos.models import *

admin.site.register(Photo, admin.OSMGeoAdmin)
admin.site.register(Brand)
admin.site.register(Camera)
admin.site.register(Lens)
admin.site.register(Media)
admin.site.register(Roll)
admin.site.register(Author)
