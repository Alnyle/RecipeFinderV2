from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from recipes.models import Category, Publisher, Level
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
    if not request.user.is_authenticated:
        return render(request, reverse("login_view"))
    return render(request, "users/profile.html")


def addRecipePage(request):
    categories = Category.objects.all()
    publishers = Publisher.objects.all()
    levels = Level.objects.all()
    return render(request, "users/addRecipe.html", {
        'Categories': categories,
        'Publishers': publishers,
        'levels': levels,
    })
