from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number', 'branch', 'first_name', 'last_name', 'role')

    # def to_representation(self, instance):
    #     user = super(UserSerializer, self).to_representation(instance)
    #     role = User.objects.get(id=instance.id).role.name
    #     user.update(
    #         {
    #             'role': role
    #         }
    #     )
    #     return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_number', 'first_name', 'last_name')
