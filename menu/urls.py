from menu import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='first'),
    path('first', views.index, name='first-dish'),
    path('salad', views.index, name='salad'),
    path('dessert', views.index, name='dessert'),
    path('drinks', views.index, name='drinks'),

]