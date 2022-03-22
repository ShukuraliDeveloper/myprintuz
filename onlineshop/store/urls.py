from django.urls import path
from .views import (
    IndexView,
    ShopView,
    Singleproduct,
    CartView,
    Checkout,
    RegistrationView,
    LoginView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('products/<int:pk>', Singleproduct.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]