from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),

    path("login/", views.CustomAuthToken.as_view(), name="api-login"),
    path("logout/", views.CustomDiscardAuthToken.as_view(), name="api-logout")

]