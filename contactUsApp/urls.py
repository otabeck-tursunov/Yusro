from django.urls import path
from .views import *

urlpatterns = [
    path('newsletter-create/', NewsletterCreateAPIView.as_view()),
    path('lid-create/', LidCreateAPIView.as_view()),
]