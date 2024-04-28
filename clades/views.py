# Create your views here.
from django.views.generic import TemplateView
from clades.models import Species
from django.views.generic.detail import DetailView

class IndexView(TemplateView):
    template_name = "clades/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['species'] = Species.objects.all()
        return context

class SpeciesView(DetailView):
    model = Species
    context_object_name = 'species'
    template_name = 'clades/species_detail.html'