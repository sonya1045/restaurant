from auth_sys import views
from django.urls import path

urlpatterns = [
    path('login', views.auth_page, name='auth-page'),
    path('register/', views.registration, name='register'),
]