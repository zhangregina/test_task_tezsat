from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from products.models import Product
from .serializers import *
from .renderers import UserJSONRenderer
from .models import *


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            return CustomUser.objects.filter(product_related=user)
        except CustomUser.DoesNotExist:
            return None


# class SchoolRatingListAPIView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = serializers.StudentListSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['user__username']
#     ordering_fields = ['user__username', 'points']
#
#     def get_queryset(self):
#         user = self.request.user
#         try:
#             return models.Student.objects.filter(branch=user.student.branch)
#         except models.Student.DoesNotExist:
#             return None


    # def get_serializer_context(self):
    #     context = super(UserListAPIView, self).get_serializer_context()
    #     context.update({"request": self.request})
    #     return context

