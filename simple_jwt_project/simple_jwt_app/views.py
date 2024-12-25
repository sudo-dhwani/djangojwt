from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    """View to obtain JWT token."""
    
    pass

class ProtectedHelloWorldView(APIView):
    print("Hello World")
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, JWT-protected World!"})
# Create your views here.
