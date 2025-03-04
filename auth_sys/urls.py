from auth_sys import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', views.registration, name='register'),
    path('login/', views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)