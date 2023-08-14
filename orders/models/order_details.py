from django.db import models

# Create your models here.
class OrderDetail(models.Model):
  order = models.ForeignKey("orders.order", on_delete=models.CASCADE, related_name="orderdetails")
  photo = models.ForeignKey("photos.photo",on_delete=models.CASCADE)
  frame = models.ForeignKey("frames.frame",on_delete=models.CASCADE)
  quantity = models.IntegerField("Количество", default=1)

  @property
  def total_price(self):
      return (self.photo.price + self.frame.price) * self.quantity
  
  class Meta:
    verbose_name = "детали заказа"
    verbose_name_plural = "детали заказы"


  def __str__(self):
    return f"Фото {self.photo}, рамка {self.frame}"

