from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .models import Category, Like
from .models import Product, Brand, ShopProduct
# Create your views here.
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse




class ProductList(ListView):
    model = Product
    template_name = 'product_list_view.html'

    def get_queryset(self):
        slug = self.kwargs.get('category_slug')
        value = self.request.GET.get('brand', None)
        category_list = super().get_queryset().filter(
            Q(category__slug=slug) | Q(category__parent__slug=slug) | Q(category__parent__parent__slug=slug))
        if value:
            category_list = category_list.filter(brand__name=value)
        return category_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_category'] = Category.objects.filter(parent=None)
        context['brand'] = Brand.objects.filter(product__in=self.get_queryset())
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
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context['']


@csrf_exempt
def product_like(request):
    get_pid = request.POST.get('pid')
    prd = Product.objects.filter(id=get_pid).first()
    lk = Like.objects.filter(product=prd, user=request.user)
    if lk.exists():
        lk.delete()
    else:
        Like.objects.create(product=prd, user=request.user)
    return HttpResponse('salam')
