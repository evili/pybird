from pybird.models import BaseNamed
from django.contrib.gis.db import models


class Zone(BaseNamed):
    area = models.PolygonField(geography=True)
