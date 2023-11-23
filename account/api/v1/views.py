from rest_framework.generics import GenericAPIView
from .serializers import RegisterSer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

import jwt
from django.conf import settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView


class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSer

    def post(self, request, *args, **kwargs):
        ser = RegisterSer(data=request.data)
        if ser.is_valid():
            ser.save()
            data = {"username": ser.validated_data["username"]}
            user_obj = get_object_or_404(
                User, username=ser.validated_data["username"]
            )
            token = self.get_tokens_for_user(user_obj)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)

class CustomDiscardAuthToken(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })