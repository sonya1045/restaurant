from django.shortcuts import render, redirect
from .models import Dish
from django.views.generic import ListView
from .forms import DishFilterForm

class DishListView(ListView):
    model = Dish
    context_object_name = 'dishes'
    template_name = 'restaurant/index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context["form"] = DishFilterForm(self.request.GET)
        return context

