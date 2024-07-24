from rest_framework import serializers
from .models import *


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'


class DiscussionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = ('full_name', 'email', 'phone_number', 'message_goal', 'message')


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class NewsletterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('phone_number',)


class LidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lid
        fields = '__all__'


class LidPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lid
        fields = ('full_name', 'phone_number', 'message')
