from django.db import models

# Create your models here.

class Frame(models.Model):
  class Fram_type(models.TextChoices):
    WOODEN = "WOODEN", "Деревянные"
    GLASS = "GLASS", "Стеклянные"
    METAL = "METAL", "Металлические"
    CERAMIC = "CERAMIC", "Керамические"
    PLUSH = "PLUSH", "Плюшевые"

  frame = models.CharField("Рамки", choices=Fram_type.choices, default=Fram_type.WOODEN,max_length=25)

  class Sise(models.TextChoices):
    ONE = "ONE", "9х13 см"
    TWO = "TWO","9х13 см"
    THREE = "THREE", "15х20 см"
    FOUR = "FOUR", "20х30 см"
  size = models.CharField("Размеры", choices=Sise.choices, default=Sise.ONE, max_length=25)
  photographer = models.ForeignKey("photographers.photographer", on_delete=models.CASCADE, related_name="frames")
  price = models.FloatField("цена")
  class Meta:
    verbose_name = "рамка"
    verbose_name_plural = "рамки"
  
  def __str__(self):
    return f"{self.frame}"


  


