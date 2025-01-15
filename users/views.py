from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# def user_list(request):
#     books = User.objects.all()
#     return render(request, 'users/user_list.html', {'users': users})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_borrowing_history')  # Redirect to a page after login
    return render(request, 'login.html')  # The login form template

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout(request):
    logout(request)  # Log out the user
    return redirect('home')  # Redirect to the homepage after logout
