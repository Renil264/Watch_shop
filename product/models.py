from django.db import models

from users.models import User


# Create your models here.
# Модели = таблици БД

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='product_images', blank=True)
    image1 = models.ImageField(upload_to='product_images', blank=True)
    image2 = models.ImageField(upload_to='product_images', blank=True)
    image3 = models.ImageField(upload_to='product_images', blank=True)
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    product_code = models.IntegerField(default=0)
    exist = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=64, blank=True)
    brand_name = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=12, blank=True)
    mechanism = models.CharField(max_length=64, blank=True)
    case_material = models.CharField(max_length=64, blank=True)
    waterproof = models.CharField(max_length=64, blank=True)
    warranty = models.CharField(max_length=64, blank=True, default=12)
    quantity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price


class FilterBrand(models.Model):
    brand = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Brand filter'

    def __str__(self):
        return self.brand


class FilterCountry(models.Model):
    country = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Country filter'

    def __str__(self):
        return self.country


class FilterMaterial(models.Model):
    material = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Material filter'

    def __str__(self):
        return self.material
