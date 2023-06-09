from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'phone_number')


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'first_name', 'last_name', 'password',
                  'phone_number', 'is_active', 'is_staff')
