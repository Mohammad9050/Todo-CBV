from django.urls import path
from . import views

urlpatterns = [
    path('',views.TaskList.as_view(), name='home'),
    path('complete/<int:pk>/', views.TaskComplete.as_view(), name='complete'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
    path('create/', views.TaskCreate.as_view(), name='create')
    
]
