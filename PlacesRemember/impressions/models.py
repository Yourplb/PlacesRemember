from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
# Create your models here.


class Impressions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True)
    created = models.DateTimeField("Создан", auto_now_add=True)

    location = PlainLocationField(based_fields=['title'], zoom=7, verbose_name='Местоположение')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

        verbose_name = "Впечатление"
        verbose_name_plural = "Впечатления"
