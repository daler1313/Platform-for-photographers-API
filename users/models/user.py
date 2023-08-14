from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField("Имя пользователя", max_length=50)
  first_name = models.CharField("Имя", max_length=65)
  last_name = models.CharField("Фамилия", max_length=65)
  email = models.EmailField("Эл.почта")
  password = models.CharField("Пароль", max_length=65)

  class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"


  def __str__(self):
    return f"{self.username}"


