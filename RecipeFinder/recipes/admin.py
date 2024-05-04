from django.contrib import admin

# Register your models here.

from .models import Category, Recipe, Ingredient, RecipeIngredient, Level, Publisher, Bookmark


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class CategoryAdmin(admin.ModelAdmin):
    list_display = "name"


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("quantity", "description")


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "date", "duration")

admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(Level)
admin.site.register(Publisher)
admin.site.register(Bookmark)
