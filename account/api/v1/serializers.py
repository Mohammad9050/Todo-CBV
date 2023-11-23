from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class RegisterSer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "password doesnt match"}
            )
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_date):
        validated_date.pop("password1", None)
        return User.objects.create_user(**validated_date)