from django.db import models
from django.conf import settings



class Photographer(models.Model):
  users = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  bio = models.TextField("БИО")

  class Meta:
    verbose_name = "Фотограф"
    verbose_name_plural = "Фотографы"
    ordering = ['users']


  def __str__(self):
    return f"Фотограф {self.users}"



