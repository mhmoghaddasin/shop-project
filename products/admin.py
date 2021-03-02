from django.contrib import admin
from .models import Category, Product, Brand, ShopProduct, Like, ProductMeta, Image, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ShopProduct)
admin.site.register(Like)
admin.site.register(ProductMeta)
admin.site.register(Image)
admin.site.register(Comment)