from django.urls import path
from .views import *

urlpatterns = [
    path('places/', PlacesListAPIView.as_view()),
    path('tour-packs/', TourPacksListAPIView.as_view()),
]
