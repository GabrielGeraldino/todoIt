from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('task/tasks')
        else:
            messages.success(request, ("Usuario ou senha incorretos"))
            return redirect('/')
    else:
        return render(request, 'auth/login.html', {})
    
def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'auth/register.html')

def logout_view(request):
    logout(request)
    redirect('login')