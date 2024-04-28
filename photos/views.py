from django.views.generic import DetailView, TemplateView
from photos.models import Photo


class PhotosIndex(TemplateView):
    template_name 'photos/index.html'


class PhotoDetailView(DetailView):
    model = Photo


def all_kml(request):
    locations = Photo.objects.kml()
    return render_to_kml("placemarks.kml", {'places': locations})
