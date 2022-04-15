from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexCreateView.as_view(), name='index'),
    path('catalog/', views.catalogView, name='catalog'),
    path('about/', views.aboutView, name='about'),
    path('price/', views.invoiceView, name='price'),
    path("pdf/", views.pdf_export, name='pdf-export'),
]
