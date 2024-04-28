# import datetime
from haystack import indexes
from clades.models import Species
# , CommonName


class SpeciesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    genus = indexes.CharField(model_attr='genus', faceted=True)

    def get_model(self):
        return Species

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
