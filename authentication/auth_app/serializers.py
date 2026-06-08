from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def create(self, validated_data):
        # removes password of the validated data
        password = validated_data.pop('password')
        user = User(**validated_data)
        # encrypts password and asigns it to user
        user.set_password(password)
        user.save()
        
        return user
    

class LoginSerializer(TokenObtainPairSerializer):
    "Automatically verifies user's credentials and creates a refresh and access token"
    pass


class ProfileSerializer(serializers.ModelSerializer):
    "Retrieves user's profile info. It also converts User model into JSON and vice versa"
    class Meta:
        model = User
        fields = ['id', 'username']