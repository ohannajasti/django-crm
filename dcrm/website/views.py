from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # django will handle the auth
from django.contrib import messages # pop up message login and out

# Create your views here.

def home(request):
    # check to see if loggin in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error Logging In. Please try again..')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')