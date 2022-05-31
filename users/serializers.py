from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        lookup_field = 'id'
        fields = ['id', 'email', 'product_related']

        # def create(self, validated_data):
        #     user = self.context['request'].user
        #     # print("User is")
        #     print(user)


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
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has not been activated.'
            )
        return {
            'email': user.email,
            'token': user.token
        }
