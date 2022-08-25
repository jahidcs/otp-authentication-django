from pyexpat import model
from rest_framework import serializers
from .models import UserLog


class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ['phone']

class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ['phone', 'otp']
