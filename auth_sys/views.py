from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate
from auth_sys.forms import UserForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def auth_page(request):
    if request.user.is_authenticated:
        return redirect('first')
    users = CustomUser.objects.get()
    context = {
        'user': users
    }
    return render(request, 'auth_sys/index.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            print('sucsess')
            return redirect('register')
            
    else:
        form = UserForm()
    return render(request, 'auth_sys/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':


        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user) 
            return redirect("dish-list")
        else:
            messages.error(request, "Wrong login or password")


    return render(request, "auth_sys/login.html")