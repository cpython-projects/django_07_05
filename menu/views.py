from django.shortcuts import render
from django.http import HttpResponse

from .models import MenuCategory


# Create your views here.
def main_menu(request):
    categories = MenuCategory.objects.filter(is_visible=True)
    return render(request, 'index.html', context={
        'categories': categories,
    })


def dish_view(request, id):
    return HttpResponse(f"<h1>Dish info #{id}</h1>")