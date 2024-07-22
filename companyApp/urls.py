from django.urls import path
from .views import *

urlpatterns = [
    path('informations/', CompanyInformationAPIView.as_view()),
]
