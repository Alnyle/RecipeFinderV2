from django import template
from django.contrib.auth.models import User
from recipes.models import Recipe, RecipeIngredient, Bookmark
register = template.Library()


@register.filter(name='check_bookmark')
def check_bookmark(user, recipe_id):
    return Bookmark.objects.filter(user=user, recipe_id=recipe_id).exists()
