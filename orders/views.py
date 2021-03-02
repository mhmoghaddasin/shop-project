from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.views.generic import ListView
from .models import Basket, BasketItem, OrderItem, Payment, Order

class BasketView(ListView):
    model = BasketItem
    template_name = 'component/basket.html'

    def get_queryset(self):
        basket_pk = super().get_queryset().filter(basket__pk=self.kwargs.get('pk'))
        return basket_pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = Basket.objects.all()



