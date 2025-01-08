from django.shortcuts import render, redirect
from .models import Dish


def index(request):
    if request.method == "POST":
        return redirect("room-detail", pk=Dish.number)
    else:
        dishes = Dish.objects.all()
        context = {
            "dishes": dishes,
        }
        return render(request, "restaurant/index.html", context)