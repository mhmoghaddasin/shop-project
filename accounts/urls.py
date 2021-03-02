from django.urls import path, include
from .views import SingUpView, ProfileView
from .views import signin, ShopView
from django.contrib.auth import urls
urlpatterns = [
    path('signup/', SingUpView.as_view(), name='SignUp'),
    path('signin/', signin, name='SignIn'),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('shop/<slug:slug>', ShopView.as_view(), name='shop_product')
]
