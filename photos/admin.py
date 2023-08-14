from django.contrib import admin
from .models import Category
from .models import Photo

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("title", "description")
  search_fields = ("title",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
  list_display = ("photographer", "title", "description","image", "price", "created_at")
  date_hierarchy = 'created_at'

