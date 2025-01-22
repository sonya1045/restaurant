from auth_sys import views
from django.urls import path

urlpatterns = [
    path('', views.auth_page, name='first'),
    path('auth/', views.auth_page, name='auth-page'),
    path('register/', views.registration, name='register'),
]