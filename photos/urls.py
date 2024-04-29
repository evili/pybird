from django.urls import path
from .views import PhotosIndex, PhotoDetailView

urlpatterns = [
    path('', PhotosIndex.as_view(), name='home'),
    path('detail/<int:id>/', PhotoDetailView.as_view(), name='photo_detail'),
]
