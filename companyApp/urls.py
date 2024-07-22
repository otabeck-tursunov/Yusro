from django.urls import path
from .views import *

urlpatterns = [
    path('informations/', CompanyInformationAPIView.as_view()),
    path('members/', MembersListAPIView.as_view()),
    path('services/', ServicesListAPIView.as_view()),
    path('comforts/', ComfortsListAPIView.as_view()),
    path('partnerships/', PartnerShipsListAPIView.as_view()),
    path('testimonials/', TestimonialsListAPIView.as_view()),
    path('questions/', QuestionsListAPIView.as_view()),
]
