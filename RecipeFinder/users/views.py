from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
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
            return JsonResponse({'message': 'User has been authenticate successfully'}, status=200)
        else:
            return JsonResponse({'message': 'Password or username is incorrect'}, status=404)
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
            return JsonResponse({'message': 'User Created'}, status=200)
        else:
            data = {'error': error, 'value': value}
            return JsonResponse(data, status=403)

    return render(request, "users/register.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html")


def profile(request):
    Categories = Category.objects.all()
    if not request.user.is_authenticated:
        return redirect(reverse('users:login_view'))
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
    # 1 - get the recipe using id
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    Categories = Category.objects.all()
    levels = Level.objects.all()
    Publishers = Publisher.objects.all()
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    # if the request method was POST then form info
    if request.method == 'POST':
        form = request.POST

        # 2- get the data from the form
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


# add a level name to recipe
def addLevel_view(request):
    if request.method == 'POST':
        level_name = request.POST.get('level_name')

        # check if the level name already exist
        if Level.objects.filter(name=level_name).exists():
            message = 'Level name already exists'
            return JsonResponse({'message': 'Level name already exists'}, status=400)

        level = Level.objects.create(name=level_name)
        return HttpResponse(status=200)
    else:
        return render(request, "users/AddLevelForm.html")


def EditLevel_view(request):
    levels = Level.objects.all()
    return render(request, 'users/EditLevel.html', {
        'levels': levels
    })


def deleteLevel_view(request):
    if request.method == 'POST':
        level_name = request.POST.get('level_name')
        try:
            level = Level.objects.get(name=level_name)
            level.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


def AddCategory_view(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')

        # check if the level name already exist
        if Category.objects.filter(name=category_name).exists():
            message = 'Category name already exists'
            return JsonResponse({'message': 'this category name already exists'}, status=400)

        category = Category.objects.create(name=category_name)
        return HttpResponse(status=204)
    else:
        return render(request, "users/AddCategoryForm.html")


# def EditCategory_view(request):
#     Categories = Category.objects.all()
#     return render(request, "users/EditCategory.html", {
#         'Categories': Categories,
#     })
#
def EditLevelForm_view(request):
    if request.method == 'POST':
        form = request.POST
        origin_name = form.get('origin_name')
        new_name = form.get('new_name')

        level = Level.objects.get(name=origin_name)
        level.name = new_name
        level.updateLevel()
        return JsonResponse({'message': 'Level name has been updated'}, status=200)

    else:
        level_name = request.GET.get('origin_name')
        level = Level.objects.get(name=level_name)
        return render(request, 'users/EditLevelForm.html', {
            'level': level
        })


def EditCategory_view(request):
    Categories = Category.objects.all()
    return render(request, "users/EditCategory.html", {
        'Categories': Categories,
    })


def deleteCategory_view(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        try:
            category = Category.objects.get(name=category_name)
            category.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


def EditCategoryForm_view(request, category_id):
    if request.method == 'POST':
        form = request.POST
        category_name = form.get('category_name')
        category = Category.objects.get(pk=category_id)

        category.name = category_name
        category.save()

        return JsonResponse({'message': 'Category name has been updated'}, status=200)
    else:
        category = Category.objects.get(pk=category_id)
        return render(request, "users/EditCategoryForm.html", {
            'category': category,
        })


def addPublisher_view(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        job_title = form.get("job_title")
        bio = form.get("bio")

        publisher = Publisher.objects.create(
            name=name,
            jobTitle=job_title,
            Bio=bio,
        )
        return HttpResponse(status=204)
    else:
        return render(request, "users/AddPublisherForm.html")


def EditPublisher_view(request):
    Publishers = Publisher.objects.all()
    return render(request, 'users/EditPublisher.html', {
        'Publishers': Publishers,
    })


def deletePublisher_view(request):
    if request.method == 'POST':
        pub_id = request.POST.get('publisher_id')
        try:
            publisher = Publisher.objects.get(pk=pub_id)
            publisher.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


def EditPublisherDetails_view(request, pub_id):
    # 1 - get the publisher using id
    publisher = get_object_or_404(Publisher, pk=pub_id)

    # if the request method was POST then get data form the info
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        jobTitle = form.get('job_title')
        Bio = form.get('bio')

        publisher.name = name
        publisher.jobTitle = jobTitle
        publisher.Bio = Bio

        publisher.UpdatePubInfo()

        return redirect('users:EditPublisher_view')

    else:
        return render(request, 'users/EditPublisherForm.html', {
            'publisher': publisher,
        })
