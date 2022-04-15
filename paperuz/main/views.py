from __future__ import unicode_literals
from django.db.models import F
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView
)
from .models import (
    Comment,
    Product,
    Category,
    Portfolio,
    Article,
    Currency,
)
from .forms import CommentForm
from django.template.loader import get_template
import pdfkit
from django.http import HttpResponse

import os
from django.conf import settings


class IndexCreateView(CreateView, ListView):
    form_class = CommentForm
    template_name = 'index.html'
    context_object_name = 'comments'
    queryset = Comment.objects.all()
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = Category.objects.all()
        context = {
            'products': data,
        }
        return context


def catalogView(request):
    products = Product.objects.all()
    articles = Article.objects.all()[:6]
    context = {
        'products': products,
        'articles': articles,
    }
    return render(request, 'catalog.html', context=context)


def aboutView(request):
    queryset = Portfolio.objects.all()[:6]
    context = {
        'portfolios': queryset
    }
    return render(request, 'about.html', context=context)


# class InvoiceView(ListView):
#     template_name = 'price.html'
#     queryset = Category.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         cat_list = []
#         products = Product.objects.all()
#         for cat in self.queryset:
#             cat['products'] = Product.objects.filter(category_id=cat.id)
#             cat_list.append(cat)
#         print("--------------------")
#         print(cat_list)
#         data = {
#             'categories': self.queryset,
#             'products': products,
#         }
#         return data


def invoiceView(request):
    categories = Category.objects.all()

    # products = Product.objects.all()
    #
    # pro = Product.objects.annotate(total_price=F('currency') * F('price_dol'))
    # currency_sum = []
    # for i in pro:
    #     currency_sum.append(i.total_price)

    context = {
        # 'categories_all': categories_all,
        'categories': categories,

    }
    return render(request, 'price.html', context=context)


import os
from django.conf import settings


def pdf_export(request):
    invoice_path = os.path.join(settings.BASE_DIR, 'templates\pdf\invoice.html')
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    products_count = Product.objects.all().count()

    count_n = list(range(1, products_count))
    css = os.path.join(settings.BASE_DIR, "static", "css", "pdf.css")

    # template = get_template('buses/pdf.html')
    products = Product.objects.all()
    currency = Currency.objects.all()
    if currency:
        for c in currency:
            if c.currency_type == "долларов":
                for pro in products:
                    pro.currency = pro.price_dol * c.summa
                    pro.save()
            else:
                continue
    category = Category.objects.all()
    categories = zip(category, count_n)
    template = get_template('pdf/invoice.html')
    html = template.render({'categories': categories, 'currency':currency})
    pdf = pdfkit.from_string(html, css=css, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=""'

    return response
