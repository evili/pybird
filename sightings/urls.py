from django.urls import path
from sightings.views import SightingView, IndexView

urlpatterns = [
    path('sighting/<int:id>/',
        SightingView.as_view(),
        name='sighting_detail'),
    path('', IndexView.as_view(), name='home'),
]
