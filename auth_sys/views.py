from django.shortcuts import render, redirect
from django.contrib.auth import login
from auth_sys.forms import UserForm
from .models import CustomUser

def auth_page(request):
    users = CustomUser.objects.all()
    if request.user.is_authenticated:
        return redirect('first')
    return render(request, 'auth_sys/log_in.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'auth_sys/register.html', {'form': form})