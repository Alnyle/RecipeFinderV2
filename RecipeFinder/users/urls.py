from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('resgister/', views.sign_up, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile, name='profile'),
    path('addRecipe/', views.addRecipePage, name='addRecipePage')
]