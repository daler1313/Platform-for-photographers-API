from django.db import models
from django.conf import settings


class Order(models.Model):
  class Status(models.TextChoices):
    PENDING = "PENDING", "В ожидании"
    CONFIRMED = "CONFIRMED", "Подтвержден"
    COMPLETED = "COMPLETED", "Выполнен"
    CANCELED = "CANCELED", "Отменен"

  status = models.CharField("статус заказа", choices=Status.choices, default=Status.PENDING, max_length=25)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
  created_at = models.DateTimeField("дата и время заказа")

  class Meta:
    verbose_name = "заказа"
    verbose_name_plural = "заказы"

  def __str__(self):
    return f"{self.user}"
