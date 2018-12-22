from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'password', 'age', 'longitude', 'latitude', 'location_text', 'aboutMe')
