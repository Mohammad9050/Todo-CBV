from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
routers.register("tasks", views.TaskView, basename="tasks")

app_name = "api"
urlpatterns = routers.urls
