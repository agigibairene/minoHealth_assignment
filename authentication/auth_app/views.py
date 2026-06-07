from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer