from django.db import models

from recipes.models import Recipe


# Create your models here.

class Favorites(models.Model):
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return f"my favorites recipe are {self.recipes}"


# it's customer
class Foodie(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=64)
    myFavorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='myFavorites')

    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.email}, {self.myFavorites}"

    def register(self):
        self.save()

    @staticmethod
    def getFoodieByEmail(email):
        try:
            return Foodie.objects.get(email=email)
        except:
            return False

    def passwordExist(self):
        if Foodie.objects.filter(password=self.password):
            return True
        return False

    def emailsExist(self):
        if Foodie.objects.filter(email=self.email):
            return True
        return False


