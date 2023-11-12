from django.shortcuts import render
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'sign_up.html'
    success_url = reverse_lazy('home')
    form_class = SignUpForm
    success_message = "Your profile was created successfully"


class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    fields = "username", "password"

    def get_success_url(self):
        return reverse_lazy("home")
    


    