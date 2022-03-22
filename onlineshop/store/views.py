from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


# def indexview(request):
#     model = Product.objects.all()
#     latest_model = model.order_by('-date_created')[:4]
#     stars = Product.objects.order_by('stars').first()
#     context = {
#         'products': model,
#         'latest': latest_model,
#         'stars': stars,
#     }
#     return render(request, 'index.html', context)


class IndexView(ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        queryset = self.model.objects.order_by('-date_created')[:3]
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'latest_products': self.get_queryset(),
            'products': self.model.objects.all(),
            'top_products': self.model.objects.order_by('stars')[:3]
        }
        return context


class ShopView(TemplateView):
    model = Product
    context_object_name = 'latest_products'
    template_name = 'shop.html'


class Singleproduct(DetailView):
    model = Product
    template_name = 'single-product.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        k = self.model.objects.first()
        context = {
            'products': self.get_queryset(),
            'products_project': k,
            'recommended_products': self.model.objects.all()[1:]
        }
        return context


class CartView(TemplateView):
    template_name = 'cart.html'


class Checkout(TemplateView):
    template_name = 'checkout.html'


class RegistrationView(TemplateView):
    template_name = 'registration.html'


class LoginView(TemplateView):
    template_name = 'login.html'
