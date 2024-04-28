from pybird.models import BaseObject
from django.contrib.gis.db import models
from photos.models import Photo, Author
from clades.models import Species
from locations.models import Zone


class Sighting(BaseObject):
    date = models.DateField()
    zone = models.ForeignKey(Zone)
    species = models.ForeignKey(Species)
    photo = models.ForeignKey(Photo, blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{0} @ {1} on {2}".format(self.species, self.zone, self.date)
