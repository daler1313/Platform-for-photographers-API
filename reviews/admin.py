from django.contrib import admin
from .models import Review
# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display = ("photo", "user", "rating", "comment", "created_at")
  search_fields = ("rating", "user")
  date_hierarchy = 'created_at'
