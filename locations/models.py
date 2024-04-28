from pybird.models import BaseObject, BaseNamed
from django.contrib.gis.db import models

# Create your models here.
class Zone(BaseNamed):
    area    = models.PolygonField(geography=True)
