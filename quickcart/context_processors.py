# -*- coding: utf-8 -*-
from products.models import Category, Product
from quickcarthome.models import Banner


def category_details(request):
    categories = Category.objects.all()
    return {"categories": categories}


def banner_details(request):
    banners = Banner.objects.all()
    return {"banners": banners}


def product_details(request):
    products = Product.objects.all().order_by("-activate_date")[:9]
    return {"products": products}
