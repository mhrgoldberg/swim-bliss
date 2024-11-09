from rest_framework import serializers
from .models import User  # Adjust the import based on your actual User model location


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
