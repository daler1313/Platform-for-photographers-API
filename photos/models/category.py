from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField("Заголовок", max_length=50)
  description = models.TextField("Описание")

  class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категории"

  def __str__(self):
    return f"{self.title}"
