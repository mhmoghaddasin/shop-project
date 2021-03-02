from django.urls import path
from .views import BasketView

urlpatterns = [
    path('basket/<int:pk>/', BasketView.as_view(), name='basket'),
]