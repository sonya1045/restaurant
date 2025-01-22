from menu import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='first'),

]