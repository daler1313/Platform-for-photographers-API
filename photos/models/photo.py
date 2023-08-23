from django.db import models

# Create your models here.

class Photo(models.Model):
  photographer = models.ForeignKey( "photographers.photographer", on_delete=models.CASCADE)
  title = models.CharField("Заголовок", max_length=50)
  description = models.TextField("Описание")
  image = models.ImageField(upload_to='images/')
  category = models.ManyToManyField("photos.category", related_name="photos")
  created_at = models.DateField("создан в")
  price = models.FloatField("цена")
  

  class Meta:
    verbose_name = "Фото"
    verbose_name_plural = "Фотки"

  def __str__(self):
    return f"{self.title}"

