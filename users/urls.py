from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('userprofile/', UserListAPIView.as_view()),
]




