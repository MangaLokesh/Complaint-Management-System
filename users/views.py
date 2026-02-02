from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
print(User.objects.all())
user=User.objects.all()
for i in user:
    print(i)
from rest_framework.permissions import AllowAny


def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")

@api_view(["POST"])
@permission_classes([AllowAny])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"error": serializer.errors}, status=400)

    username = serializer.validated_data["username"]
    email = serializer.validated_data.get("email", "")
    password = serializer.validated_data["password"]
    password2 = serializer.validated_data["password2"]
   
    if password != password2:
        return Response({"error": "Passwords do not match"}, status=400)

    
    if User.objects.filter(username=username).exists():
        return Response({"error": {"username": ["Username already exists"]}}, status=400)

   
    if email and User.objects.filter(email=email).exists():
        return Response({"error": {"email": ["Email already exists"]}}, status=400)
    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({"message": "User registered successfully ✅"}, status=201)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "username": request.user.username,
        "is_superuser": request.user.is_superuser
    })