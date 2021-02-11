from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SlideShow
from products.models import Category, Product

# Create your views here.

class HomeView(TemplateView):
    template_name = "./index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShow.objects.all()
        context['category_list'] = Category.objects.filter(parent=None)
        context['products'] = Product.objects.all()
        return context

