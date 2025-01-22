from django.shortcuts import render, redirect
from django.contrib.auth import login
from auth_sys.forms import UserForm
from .models import User

def auth_page(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_sys/index.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'auth_sys/register.html', {'form': form})

def edit_profile(request_user, profile_user):
    # Користувач може редагувати свій профіль
    if request_user == profile_user:
        return True 
    return False