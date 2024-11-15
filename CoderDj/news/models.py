from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class News_post(models.Model):  # Рекомендуется использовать `CamelCase` для имен моделей
    title = models.CharField("Название новости", max_length=50)
    short_description = models.CharField("Краткое описание", max_length=200)
    text = models.TextField("Новость")
    pub_date = models.DateTimeField("Дата публикации")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
