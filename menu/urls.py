from menu import views
from django.urls import path
from .views import DishListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.DishListView.as_view(), name='dish-list'),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)