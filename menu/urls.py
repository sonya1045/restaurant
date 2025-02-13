from menu import views
from django.urls import path
from .views import DishListView

urlpatterns = [
    path('', views.DishListView.as_view(), name='first'),
    path('first', views.DishListView.as_view(), name='first-dish'),
    path('salad', views.DishListView.as_view(), name='salad'),
    path('dessert', views.DishListView.as_view(), name='dessert'),
    path('drinks', views.DishListView.as_view(), name='drinks'),
    path('<int:pk>', views.DishListView.as_view(), name='dishes'),

]                                       