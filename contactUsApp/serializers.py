from rest_framework import serializers
from .models import *


class NewsletterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('phone_number',)


class LidPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lid
        fields = ('full_name', 'phone_number', 'message')
