from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from recipes.models import Category, Publisher, Level, Recipe, RecipeIngredient, Bookmark, RecipeForm, Level
from .models import Foodie

from recipes import views


# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            print("invalid Email")
            return render(request, "users/login.html", {
                'message': "invalid username or password"
            })
    return render(request, "users/login.html")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        # access form info
        firstname = request.POST["firstName"]
        lastname = request.POST["lastName"]
        password = request.POST["password"]
        email = request.POST["email"]
        isAdmin = request.POST.get("isAdmin", False)

        value = {
            'firstname': firstname,
            'lastname': lastname,
            'password': password,
            'email': email,
        }

        error = None
        # validate Foodie email and password if are exist
        if User.objects.filter(email=email).exists():
            error = "Email already Exist"
        elif User.objects.filter(password=password).exists():
            error = "Password already Exist"

        if not error:
            firstname = firstname.lower()
            lastname = lastname.lower()
            user = User.objects.create_user(username=firstname, password=password, email=email, first_name=firstname,
                                            last_name=lastname)
            # if is admin register as admin
            if isAdmin:
                user.is_staff = True
                user.is_superuser = True
            user.save()
            return redirect(reverse('index'))
        else:
            data = {'error': error, 'value': value}
            return render(request, "users/register.html", {
                'data': data
            })

    return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html")


def profile(request):
    Categories = Category.objects.all()
    if not request.user.is_authenticated:
        return render(request, reverse("login_view"))
    return render(request, "users/profile.html", {
        'Categories': Categories,
    })


def addRecipePage(request):
    categories = Category.objects.all()
    publishers = Publisher.objects.all()
    levels = Level.objects.all()
    return render(request, "users/addRecipe.html", {
        'Categories': categories,
        'Publishers': publishers,
        'levels': levels,
    })


def editRecipePage(request):
    recipes = Recipe.objects.all()
    RecipeIngredients = RecipeIngredient.objects.all()
    bookmarks = None
    categories = None
    Categories = Category.objects.all()

    # if user authenticated and have saved recipe get them
    if request.user.is_authenticated:
        user = request.user
        bookmarks = Bookmark.objects.filter(user=user).select_related("recipe")

    return render(request, "users/EditRecipe.html", {
        'recipes': recipes,
        'RecipeIngredients': RecipeIngredients,
        'bookmarks': bookmarks,
        'Categories': Categories,
    })


def deleteRecipe(request, recipe_id):
    user = request.user
    if user.is_staff and user.is_superuser:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return redirect('users:profile')


def editRecipeDetails(request, recipe_id):
    # 2 - get the recipe
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Categories = Category.objects.all()
    levels = Level.objects.all()
    Publishers = Publisher.objects.all()
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    # if the request method was POST then form info
    if request.method == 'POST':
        form = request.POST

        # 1- get the data from the form
        recipeName = form.get('recipe_name')
        category_id = form.get('course_name')
        recipeImage = request.FILES.get('recipe_image')
        publisher_id = form.get('publisher')
        level_name = form.get('recipe_level')
        duration = form.get('recipe_duration')
        steps = form.get('recipe_steps')

        # 3-  if recipe image is exist in the form then save as url
        if recipeImage is not None:
            fs = FileSystemStorage()
            filename = fs.save(recipeName, recipeImage)
            uploaded_file_url = fs.url(filename)
            recipe.image_link = uploaded_file_url

        recipeDescription = form.get('recipe_description')
        # category = get_object_or_404(Category, id=category_id)
        publisher = get_object_or_404(Publisher, id=publisher_id)
        level = get_object_or_404(Level, name=level_name)

        # categoryI = Category.objects.get(pk=category_id)

        recipe.name = recipeName
        recipe.publisher = publisher
        recipe.description = recipeDescription
        recipe.duration = duration
        recipe.Level = level
        recipe.recipes = category_id,
        recipe.steps = steps

        recipe.updateRecipe()

        return redirect('users:editRecipePage')

    else:
        return render(request, 'users/editRecipeDetails.html', {
            'recipe': recipe,
            'Categories': Categories,
            'levels': levels,
            'Publishers': Publishers,
            'ingredients': ingredients,
        })
