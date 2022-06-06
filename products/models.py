from django.db import models
from users.models import *


class Category(models.Model):
    title = models.CharField(max_length=25)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='photo', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  # при удалении поста, удал комменты
                                related_name='product_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
