import datetime
from haystack import indexes
from sightings.models import Sighting

class SightingIndex(indexes.SearchIndex, indexes.Indexable):
    text       = indexes.CharField(document=True, use_template=True)
    sight_date = indexes.DateTimeField(model_attr='date')
    location   = indexes.LocationField(model_attr='photo__position')

    def get_model(self):
        return Sighting
