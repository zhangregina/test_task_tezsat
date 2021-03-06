from django.db import models
from users.models import *


class Product(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='photo', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  # при удалении поста, удал комменты
                             related_name='product_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)