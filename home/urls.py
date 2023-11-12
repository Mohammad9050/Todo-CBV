from django.urls import path
from . import views

urlpatterns = [
    path('',views.first, name='home'),
    path('list/', views.TaskList.as_view(), name='list'),
    path('complete/<int:pk>/', views.TaskComplete.as_view(), name='complete'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
    path('create/', views.TaskCreate.as_view(), name='create')
    
]
