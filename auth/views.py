from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PortfolioForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.http import  JsonResponse
from django.contrib.auth import get_user_model
from .models import SavedAccount

# Create your views here.
def auth_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'auth_sys/auth_page.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'templates/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            
            # Отримуємо перший збережений акаунт
            saved_account = SavedAccount.objects.filter(user=current_user).first()
            
            if saved_account:
                try:
                    User = get_user_model()
                    next_user = User.objects.get(username=saved_account.username)
                    
                    # Перевіряємо пароль
                    if next_user.check_password(saved_account.password):
                        # Видаляємо поточний акаунт зі збережених у наступного користувача
                        SavedAccount.objects.filter(
                            user=next_user,
                            username=current_user.username
                        ).delete()
                        
                        # Видаляємо наступний акаунт зі збережених у поточного користувача
                        saved_account.delete()
                        
                        logout(request)
                        login(request, next_user)
                        return JsonResponse({
                            'status': 'success',
                            'redirect_url': reverse('profile', kwargs={'username': next_user.username})
                        })
                except Exception as e:
                    print(f"Error switching account: {str(e)}")
            
            # Якщо немає збережених акаунтів або виникла помилка
            logout(request)
            return JsonResponse({
                'status': 'success',
                'redirect_url': '/'
            })
    
    # Для GET запитів
    logout(request)
    return redirect('/')


def can_edit_profile(request_user, profile_user):
    # Користувач може редагувати свій профіль
    if request_user == profile_user:
        return True
        
    # Admin може редагувати всіх
    if request_user.is_superuser:
        return True
        
    # Moderator може редагувати звичайних користувачів
    if request_user.is_staff and not profile_user.is_staff and not profile_user.is_superuser:
        return True
        
    return False