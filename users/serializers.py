from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from products.models import Product
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'products']

    def to_representation(self, instance): #переопределяет данные в зависимости от юзера кот залогинился
        data = super().to_representation(instance)
        if data['id'] == self.context['request'].user.id:
            return data


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password2', 'token']

    def validate_email(self, value):
        user = CustomUser.objects.filter(email=value)
        if user:
            raise ValidationError('User with this email already exists!')
        return value

    def create(self, validated_data):
        account = CustomUser(
            email=self.validated_data['email'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must match'}
            )
        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

