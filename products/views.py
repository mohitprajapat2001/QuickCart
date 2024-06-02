# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from products.models import Category, Product
from quickcart import constants
from django.db.models import Q
from django.core.paginator import Paginator


class ProductListView(TemplateView):
    template_name = constants.PRODUCT_LIST_VIEW

    def get_context_data(self, **kwargs):
        category_pk = kwargs["pk"]
        category_data = Category.get_categories(category_pk)
        paginator = Paginator(Category.get_product(category_pk), 9)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "category_data": category_data,
            "page_obj": page_obj,
            "category_pk": category_pk,
        }
        return context


class ProductGridView(TemplateView):
    template_name = constants.PRODUCT_GRID_VIEW

    def get_context_data(self, **kwargs):
        category_pk = kwargs["pk"]
        category_data = Category.get_categories(category_pk)
        paginator = Paginator(Category.get_product(category_pk), 9)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "category_data": category_data,
            "page_obj": page_obj,
            "category_pk": category_pk,
        }
        return context
