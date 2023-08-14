from django.db import models

# Create your models here.

class Review(models.Model):
  photo = models.ForeignKey("photos.photo", on_delete=models.CASCADE, related_name="reviews")
  user = models.ForeignKey("users.user", on_delete=models.CASCADE)

  class Rating(models.TextChoices):
    ONE = "ONE", "1"
    TWO = "TWO", "2"
    THREE = "THREE", "3"
    FOUR = "FOUR", "4"
    FIVE = "FIVE", "5"
    SIX = "SIX","6"
    SEVEN = "SEVEN","7"
    EIGHT = "EIGHT","8"
    NINE = "NINE","9"
    TEN = "TEN","10"
 
  rating = models.CharField("Рейтинг", choices=Rating.choices, default=Rating.ONE, max_length=25)
  comment = models.TextField("Комментарий")
  created_at = models.DateField("создан в")

  class Meta:
    verbose_name = "Рейтинг"
    verbose_name_plural = "Рейтингы"

  def __str__(self):
    return f"{self.rating}"


