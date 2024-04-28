from django.contrib.gis.db import models


class BaseObject(models.Model):
    version = models.DateTimeField(editable=False, auto_now=True)
    objects = models.GeoManager()

    class Meta:
        abstract = True
        get_latest_by = 'version'


class BaseNamed(BaseObject):
    name = models.CharField(max_length=63, unique=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta(BaseObject.Meta):
        abstract = True
        get_latest_by = 'version'
        ordering = ['name']

    def __unicode__(self):
        return self.name
