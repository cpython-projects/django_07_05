from django.contrib import admin
from .models import MenuCategory, Dish


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass
