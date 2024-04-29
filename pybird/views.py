from django.views.generic import TemplateView
from photos.models import Photo
from django.utils.translation import gettext as _


class IndexView(TemplateView):
    template_name = 'pybird/index.html'

    def get_context(self, *args, **kwargs):
        data = {
            'menu': [_('Photograpies'), _('Venues'), _('Clades')],
            'ls': Photo.objects.latest()
        }
        super().get_context(self, *args, **kwargs)
