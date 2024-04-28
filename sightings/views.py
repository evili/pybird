from django.views.generic import TemplateView
from sightings.models import Sighting
from django.views.generic.detail import DetailView

class IndexView(TemplateView):
    template_name = "sightings/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['species'] = Sighting.objects.all()
        return context


class SightingView(DetailView):
    model = Sighting
    context_object_name = 'sighting'
    template_name = 'sightings/sighting_detail.html'
