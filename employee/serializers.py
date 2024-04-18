from rest_framework import serializers
from .models import CustomUser, Notification

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_country_code', 'phone_number', 'profile_photo']
