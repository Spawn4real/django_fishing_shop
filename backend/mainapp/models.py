from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    short_description = models.CharField(verbose_name='Короткое описание', max_length=128, blank=True)
    categories = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    price_with_discount = models.DecimalField(verbose_name='Цена со скидкой', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во на складе', default=0)
    image = models.ImageField(upload_to='products_images', blank=True)

    def __str__(self):
        return self.name
