from rest_framework import serializers
from .models import *


class DiscussionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('full_name', 'email', 'phone_number', 'message_goal', 'message')


class NewsletterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('phone_number',)


class LidPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lid
        fields = ('full_name', 'phone_number', 'message')
