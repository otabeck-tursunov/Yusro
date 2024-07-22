from rest_framework.generics import *
from rest_framework.views import APIView

from .serializers import *
from .models import *


class DiscussionCreateAPIView(CreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionPostSerializer


class NewsletterCreateAPIView(CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterPostSerializer


class LidCreateAPIView(CreateAPIView):
    queryset = Lid.objects.all()
    serializer_class = LidPostSerializer
