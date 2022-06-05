from django.contrib.auth import login
from rest_framework import status, response, exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .renderers import UserJSONRenderer
from .models import *
from django.contrib.auth import authenticate


def get_login_response(user, request):
    refresh = RefreshToken.for_user(user)
    data = {
        "user": UserSerializer(instance=user, context={'request': request}).data,
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }
    return data


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if not user:
            raise exceptions.AuthenticationFailed()
        login(request, user)
        return Response(data=get_login_response(user, request))


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):  # отправляем данные контекстом в сериализатор
        context = super(UserListAPIView, self).get_serializer_context()
        context.update({"request": self.request})
        print(self.request)
        return context
