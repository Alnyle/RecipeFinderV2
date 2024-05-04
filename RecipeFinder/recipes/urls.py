from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('favorite/', views.favorite, name="favorite"),
    path('discover/', views.discover, name="discover"),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
    path('<int:recipe_id>/', views.recipe_details, name="recipe_details"),
    path('favorite/<int:recipe_id>', views.add_to_favorites, name="add_to_favorites"),
    path('<int:category_id>/Category', views.get_category, name="get_category"),
    path('addRecipe/', views.addRecipe, name='addRecipe'),
]
