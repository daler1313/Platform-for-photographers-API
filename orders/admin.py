from django.contrib import admin
from .models import Order,OrderDetail

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ["status", "user", "created_at"]
  date_hierarchy = 'created_at'


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
  list_display = ["order", "photo", "frame", "quantity", "total_price"]
  
