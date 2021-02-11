from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import Category
from .models import Product
# Create your views here.
from django.views.generic import DetailView


class ProductList(ListView):
    model = Product
    template_name = 'product_list_view.html'

    def get_queryset(self):
        slug = self.kwargs.get('category_slug')
        return super().get_queryset().filter(
            Q(category__slug=slug) | Q(category__parent__slug=slug) | Q(category__parent__parent__slug=slug))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_category'] = Category.objects.filter(parent=None)
        return context


    # slug = self.kwargs.get('category_slug')
    # category = get_object_or_404(Category.objects.filter(), slug=slug)
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(self.kwargs['slug'])
    #     print(queryset)
    #     return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-detail.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class Search(ListView):
    model = Product
    template_name = 'search_result.html'

    def get_queryset(self):
        search_result = self.request.GET.get('value')
        return super().get_queryset().filter(Q(name__icontains=search_result) |
                                             Q(slug__icontains=search_result) |
                                             Q(details__icontains=search_result))

