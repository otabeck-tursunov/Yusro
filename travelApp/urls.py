from django.urls import path
from .views import *

urlpatterns = [
    path('places/', PlacesListAPIView.as_view()),
    path('tour-packs/', TourPacksListAPIView.as_view()),
    path('tour-packs/<int:tour_pack_id>/', TourPackRetrieveAPIView.as_view()),
]
