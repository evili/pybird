# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml
from django.template.context import RequestContext
from photos.models import Photo
from django.http import Http404
from django.utils.translation import ugettext as _

_photos = Photo.objects

def detail(request, id=0):
    try:
        p = _photos.get(pk=id)
    except Photo.DoesNotExist:
        raise Http404    

    data = {'photo': p }

    return render_to_response(
        'photos/detail.html',
        data,
        context_instance=RequestContext(request)
        )

def all_kml(request):
    locations  = Photo.objects.kml()
    return render_to_kml("placemarks.kml", {'places' : locations}) 
    
