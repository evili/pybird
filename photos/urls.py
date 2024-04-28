from django.urls import path
from django.views.generic.simple import direct_to_template
from .views import PhotosIndex, PhotoDetail

urlpatterns = [
    path('', PhotosIndex.as_view(), name='home'),
    path('detail/<int:id>/', PhotoDetail.as_view(), name='photo_detail'),
]
