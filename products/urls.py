from django.urls import path
from .views import ProductList
from .views import ProductDetailView, Search, product_like

urlpatterns = [
    path('category/<slug:category_slug>/', ProductList.as_view(), name='category_detail'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', Search.as_view(), name='product_search'),
    path('like/', product_like, name='product_like'),
]
