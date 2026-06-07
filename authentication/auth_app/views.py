from .serializers import UserSerializer, LoginSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {'message': 'User registered successfully'},
            status=status.HTTP_201_CREATED
        )
        
        

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    