from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.conf import settings


User = get_user_model()
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(User, related_name='order', related_query_name='order', verbose_name=_('customer'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.CharField(verbose_name=_('description'), blank=True, max_length=150)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')




    def __str__(self):
        return (self.customer.name, 'order')


class OrderItem(models.Model):
    order = models.ForeignKey("Order", related_name='orderitems', related_query_name='orderitems', verbose_name=_('order'), on_delete=models.CASCADE, blank=True, null=True)
    shop_product = models.ForeignKey("products.ShopProduct", verbose_name=_('shopproduct'), related_name='orderitems', related_query_name='orderitems', on_delete=models.SET_NULL,  null=True, blank=True)
    count = models.IntegerField(verbose_name=_('count'), )
    price = models.IntegerField(verbose_name=_('price'), )

    class Meta:
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItems')

    @property
    def total_item_price(self):
        return self.count * self.price



    def __str__(self):
        return self.shop_product.product.name, self.order

class Basket(models.Model):
    customer = models.OneToOneField(User, related_name='basket', related_query_name='basket', verbose_name=_('customer'), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _('basket')
        verbose_name_plural = _('baskets')

    def __str__(self):
        return self.customer.name, 'basket'

class BasketItem(models.Model):
    basket = models.ForeignKey("Basket", verbose_name=_('basket'), related_name='basket_items', related_query_name='basket_items', on_delete=models.CASCADE, null=True , blank=True)
    shop_product = models.ForeignKey("products.ShopProduct", verbose_name=_('shop_product'), related_name='basket_items', related_query_name='basket_items', on_delete= models.CASCADE, null=True , blank=True)
    count = models.IntegerField(verbose_name=_('price'), )

    class Meta:
        verbose_name = _('basketitem')
        verbose_name_plural = _('basketitems')

    def __str__(self):
        return self.shop_product.product.name, 'basket'


class Payment(models.Model):
    order = models.OneToOneField("Order", verbose_name=_('order'), related_name='payment', related_query_name='payment', on_delete = models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(User, related_name='payment', related_query_name='payment', verbose_name=_('customer'), on_delete=models.SET_NULL, blank=True, null=True)
    total = models.IntegerField(verbose_name=_('total_price'), )
    #هزینه پرداخت

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __str__(self):
        return self.customer.name, self.total, 'payment'