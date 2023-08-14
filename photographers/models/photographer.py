from django.db import models

# Create your models here.


class Photographer(models.Model):
  users = models.OneToOneField("users.user", on_delete=models.CASCADE)
  bio = models.TextField("БИО")

  class Meta:
    verbose_name = "Фотограф"
    verbose_name_plural = "Фотографы"
    ordering = ['users']


  def __str__(self):
    return f"Фотограф {self.users}"



