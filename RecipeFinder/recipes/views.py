from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django import template
from .models import Recipe, RecipeIngredient, Bookmark, Category, Ingredient, Publisher, Level
from django.db.models import Q

from users import views

register = template.Library()


# Create your views here.


def index(request):
    # get all recipes
    recipes = Recipe.objects.all()
    RecipeIngredients = RecipeIngredient.objects.all()
    bookmarks = None
    categories = None
    family_recipes = None
    categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
    # Filter categories to include only those with associated recipes
    categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)

    last_recipes = Recipe.objects.all().order_by('-date')
    family_category = Category.objects.get(name='Family')
    family_recipes = Recipe.objects.filter(category=family_category)

    # if user authenticated and have saved recipe get them
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, "recipes/index.html", {
        'recipes': recipes,
        'RecipeIngredients': RecipeIngredients,
        'bookmarks': bookmarks,
        'Categories': categories_with_recipes,
        'last_recipes': last_recipes,
        'family_recipes': family_recipes,
        'family_category': family_category,
    })


def add_to_favorites(request, recipe_id):
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

        categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
        # Filter categories to include only those with associated recipes
        categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)


        return render(request, 'recipes/favorite.html', {
            'recipes': recipes,
            'RecipeIngredients': RecipeIngredients,
            'bookmarks': bookmarks,
            'Categories': categories_with_recipes,

        })
    else:
        # return render(request, 'recipes/favorite.html')
        return redirect(reverse('users:login_view'))


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    steps = recipe.steps.split('\n')

    categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
    # Filter categories to include only those with associated recipes
    categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)

    bookmarks = None
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, 'recipes/recipeDetails.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'steps': steps,
        'Categories': categories_with_recipes,
    })


def discover(request):
    Categories = Category.objects.all()
    print(Categories)
    return render(request, 'recipes/category.html', {
        'Categories': Categories,
    })


def get_category(request, category_id):
    bookmarks = None
    recipes = Recipe.objects.filter(category__id=category_id)

    categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
    # Filter categories to include only those with associated recipes
    categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)

    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user)

    return render(request, 'recipes/category.html', {
        "recipes": recipes,
        "bookmarks": bookmarks,
        'Categories': categories_with_recipes,
    })


def AboutUs(request):
    bookmarks = None
    categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
    # Filter categories to include only those with associated recipes
    categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)
    return render(request, 'recipes/aboutUs.html', {
        'Categories': categories_with_recipes,
    })


def addRecipe(request):
    user = request.user
    if user.is_authenticated and request.method == "POST" and user.is_superuser:
        form = request.POST
        recipeName = form.get('recipe_name')
        category_id = form.get('course_name')
        recipeImage = request.FILES.get('recipe_image')
        publisher_id = form.get('publisher')
        level_name = form.get('recipe_level')
        duration = form.get('recipe_duration')
        steps = form.get('recipe_steps')

        # check is image is not empty
        if recipeImage is None:
            default_Image = 'defaultImage'
            uploaded_file_url = default_Image
        else:
            fs = FileSystemStorage()
            filename = fs.save(recipeName, recipeImage)
            uploaded_file_url = fs.url(filename)

        recipeDescription = form.get('recipe_description')
        category = get_object_or_404(Category, id=category_id)
        publisher = get_object_or_404(Publisher, id=publisher_id)
        level = get_object_or_404(Level, name=level_name)

        new_recipe = Recipe.objects.create(
            name=recipeName,
            publisher=publisher,
            description=recipeDescription,
            duration=duration,
            Level=level,
            category=category,
            image_link=uploaded_file_url,
            steps=steps,
        )

        # recipe ingredients
        ingredientNames = form.getlist('ingredient_name')
        ingredientQuantities = form.getlist('ingredient_quantity')
        ingredientDescriptions = form.getlist('ingredient_description')
        for name, quantity, description in zip(ingredientNames, ingredientQuantities, ingredientDescriptions):
            ingredient, _ = Ingredient.objects.get_or_create(name=name)
            RecipeIngredient.objects.create(
                recipe=new_recipe,
                ingredient=ingredient,
                quantity=quantity,
                description=description
            )

        # Ingredients = form.get('ingredients')
        # Ingredients functionality does work yet
        return redirect('index')
        # return HttpResponse(status=204)

    return HttpResponse(status=302)  # find better status code


def searchRecipe(request):
    recipes = None
    bookmarks = None
    Categories = None
    RecipeIngredients = None
    if request.method == 'GET':
        form = request.GET
        query = form.get('query')
        if query:

            recipes = Recipe.objects.filter(Q(name__contains=query) | Q(description__contains=query))
        else:
            recipes = Recipe.objects.none()
        print(query)
        RecipeIngredients = RecipeIngredient.objects.all()
        categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
        # Filter categories to include only those with associated recipes
        categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)

        # if user authenticated and have saved recipe get them
        if request.user.is_authenticated:
            user = request.user
            bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, 'recipes/SearchPage.html', {
        'recipes': recipes,
        'RecipeIngredients': RecipeIngredients,
        'bookmarks': bookmarks,
        'Categories': categories_with_recipes,
    })


def allRecipe(request):
    # get all recipes
    recipes = Recipe.objects.all()
    RecipeIngredients = RecipeIngredient.objects.all()
    bookmarks = None
    categories = None
    family_recipes = None
    categories_with_recipes = Category.objects.annotate(num_recipes=Count('recipes'))
    # Filter categories to include only those with associated recipes
    categories_with_recipes = categories_with_recipes.filter(num_recipes__gt=0)

    last_recipes = Recipe.objects.all().order_by('-date')
    family_category = Category.objects.get(name='Family')
    family_recipes = Recipe.objects.filter(category=family_category)

    # if user authenticated and have saved recipe get them
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, "recipes/AllRecipes.html", {
        'recipes': recipes,
        'RecipeIngredients': RecipeIngredients,
        'bookmarks': bookmarks,
        'Categories': categories_with_recipes,
    })