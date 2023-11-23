from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("api/v1/", include("account.api.v1.urls")),
    

]
