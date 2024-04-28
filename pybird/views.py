from django.shortcuts import render_to_response
from django.template.context import RequestContext
from photos.models import Photo
from django.utils.translation import ugettext as _


def index(request):
    data = {
        'menu': [_('Photograpies'),_('Venues'),_('Clades')],
        'ls': Photo.objects.latest()
        }
    
    return render_to_response(
        'index.html',
        data,
        context_instance=RequestContext(request)
        )
