from django.urls import path
from .views import *

urlpatterns = [
    path('discussion-create/', DiscussionCreateAPIView.as_view()),
    path('newsletter-create/', NewsletterCreateAPIView.as_view()),
    path('lid-create/', LidCreateAPIView.as_view()),
]