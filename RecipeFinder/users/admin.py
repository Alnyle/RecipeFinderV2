from django.contrib import admin
from .models import Foodie


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "password", "favoriteFoodie")


admin.site.register(Foodie)
