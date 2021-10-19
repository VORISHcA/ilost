from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Название',
        unique=True,
        )

    desc = models.TextField(
        verbose_name='Описание',
        blank=True
    )

