# -*- coding: utf-8 -*-
from products.models import Category
from quickcarthome.models import Banner


def category_details(request):
    categories = Category.objects.all()
    return {"categories": categories}


def banner_details(request):
    banners = Banner.objects.all()
    return {"banners": banners}
