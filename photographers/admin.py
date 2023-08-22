from django.contrib import admin
from .models import Photographer



@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
  list_display = ["pk","users", "bio"]
