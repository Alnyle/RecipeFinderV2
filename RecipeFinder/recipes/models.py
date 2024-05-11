from django.contrib.auth.models import User
from django.db import models
from django import forms
# Create your models here.
from django.db import models


# Define Publisher model first


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    jobTitle = models.CharField(max_length=255)
    Bio = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    @staticmethod
    def get_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"level: {self.name}"


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="PublishInfo")
    description = models.TextField(null=False, blank=False)
    duration = models.PositiveIntegerField(null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, name='Level')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', related_name='recipes')
    steps = models.TextField(null=False, blank=False)
    image_link = models.CharField(max_length=1000, default='defaultImage')

    def updateRecipe(self):
        self.save()


# class Steps(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")
#     description = models.TextField(null=False, blank=False)
#     order = models.PositiveIntegerField(default=1, unique=True)

# def __str__(self):
#     return f"{self.order}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipeIngredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredients")
    quantity = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"RecipeIngredient Technique: {self.quantity}, {self.description}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipeBookmarks")

    @staticmethod
    def check_bookmark(user, recipe_id):
        return Bookmark.objects.filter(user=user) and Bookmark.objects.filter(reciep=recipe_id).exists()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'publisher', 'duration', 'category', 'ingredients', 'steps',
                  'image_link']
