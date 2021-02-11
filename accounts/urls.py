from django.urls import path
from .views import SingUpView
from .views import signin
urlpatterns = [
    path('signup/', SingUpView.as_view(), name='SignUp'),
    path('signin/', signin, name='SignIn')
]