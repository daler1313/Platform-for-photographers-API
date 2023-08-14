from django.contrib import admin
from .models import Photographer
# Register your models here.


@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
  list_display = ["users", "bio"]
