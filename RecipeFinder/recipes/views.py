from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django import template
from .models import Recipe, RecipeIngredient, Bookmark, Category

from users import views

register = template.Library()


# Create your views here.


def index(request):
    # get all recipes
    recipes = Recipe.objects.all()
    RecipeIngredients = RecipeIngredient.objects.all()
    bookmarks = None
    categories = None
    Categories = Category.objects.all()

    # if user authenticated and have saved recipe get them
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, "recipes/index.html", {
        'recipes': recipes,
        'RecipeIngredients': RecipeIngredients,
        'bookmarks': bookmarks,
        'Categories': Categories,
    })


def add_to_favorites(request, recipe_id):
    print("worked")
    if request.method == "POST":
        if request.user.is_authenticated:
            recipe = Recipe.objects.get(pk=recipe_id)
            user = request.user
            book_marked = Bookmark.objects.filter(user=user, recipe=recipe).exists()

            if book_marked:
                Bookmark.objects.filter(user=user, recipe=recipe).delete()
                return HttpResponse(status=204)
            else:
                Bookmark.objects.create(user=user, recipe=recipe)
                return HttpResponse(status=204)
        else:
            return redirect(reverse('users:login_view'))


def favorite(request):
    if request.user.is_authenticated:
        recipes = Recipe.objects.all()
        RecipeIngredients = RecipeIngredient.objects.all()
        bookmarks = None
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

        Categories = Category.objects.all()

        return render(request, 'recipes/favorite.html', {
            'recipes': recipes,
            'RecipeIngredients': RecipeIngredients,
            'bookmarks': bookmarks,
            'Categories': Categories,

        })
    else:
        # return render(request, 'recipes/favorite.html')
        return redirect(reverse('users:login_view'))


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    steps = recipe.steps.split('\n')

    bookmarks = None
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, 'recipes/recipeDetails.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'steps': steps,
    })


def discover(request):
    Categories = Category.objects.all()
    print(Categories)
    return render(request, 'recipes/category.html', {
        'Categories': Categories,
    })


def get_category(request, category_id):
    bookmarks = None
    recipes = Recipe.objects.filter(category=category_id)
    Categories = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user)

    return render(request, 'recipes/category.html', {
        "recipes": recipes,
        "bookmarks": bookmarks,
        'Categories': Categories,

    })


def AboutUs(request):
    bookmarks = None
    Categories = Category.objects.all()
    return render(request, 'recipes/aboutUs.html', {
        'Categories': Categories,
    })


def addRecipe(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        form = request.POST
        recipeName = form.get('recipe_name')
        category = form.get('course_name')
        recipeImage = form.get('recipe_image')
        recipeDescription = form.get('recipe_description')

        Ingredients = form.get('ingredients')
        # Ingredients functionality does work yet

        return HttpResponse(status=204)

    return HttpResponse(status=302) # find better status code
