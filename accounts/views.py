from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth.views import LoginView
from django.shortcuts import reverse, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .form import RegistrationForm
from .models import User, Shop
from products.models import ShopProduct

# class SingUpView(TemplateView):
#     template_name = 'SignUp.html'


def signin(request):
    if request.method == 'POST':
        request_username = request.POST.get('username', None)
        request_password = request.POST.get('password', None)
        user = authenticate(request, username=request_username, password=request_password)
        print(user, request_username, request_password)
        if user is not None:
            login(request, user)
    return redirect('home')

class SingUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'SignUp.html'

    def form_valid(self, form):
        register_form = form.save(commit=False)
        register_form.set_password(register_form.password)
        register_form.save()
        self.kwargs['pk'] = register_form.pk
        return super(SingUpView, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})

class ProfileView(DetailView):
    model = User
    template_name = 'component/profile_with_data_and_skills.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ShopView(ListView):
    model = ShopProduct
    template_name = 'shop_template.html'

    def get_queryset(self):
        return super().get_queryset().filter(shop__slug=self.kwargs.get('slug'))

