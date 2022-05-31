from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'description',
            'title',
            'image',
            # 'user_related'

        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPutSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(default=None)
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()
    image = serializers.ImageField(required=False)

    def validate_title(self, title):
        posts = Product.objects.filter(title=title)
        if posts:
            raise ValidationError('This product already exists!!')
        return title
