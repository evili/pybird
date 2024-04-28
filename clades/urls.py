from django.urls import path
from clades.views import IndexView, SpeciesView

urlpatterns = [
        path('species/<int:id>/', SpeciesView.as_view(),
            name='species-detail'),
        path('', IndexView.as_view(), name='home'),
]
