from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
# from l.models import Owner


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [AllowAny]


def submit(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {'username': username})
    return render(request, 'login.html')