from django.contrib import admin
from .models import Order, OrderItem, Basket, BasketItem, Payment
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Basket)
admin.site.register(BasketItem)
admin.site.register(Payment)
