from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


class SingUpView(TemplateView):
    template_name = 'SignUp.html'


def signin(request):
    if request.method == 'POST':
        request_username = request.POST.get('username', None)
        request_password = request.POST.get('password', None)
        user = authenticate(request, username=request_username, password=request_password)
        print(user, request_username, request_password)
        if user is not None:
            login(request, user)
    return HttpResponse('s')
