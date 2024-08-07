# -*- coding: utf-8 -*-
from django.urls import path
from products.views import ProductListView, ProductGridView

urlpatterns = [
    path("listview/<int:pk>", ProductListView.as_view(), name="list-product"),
    path("gridview/<int:pk>", ProductGridView.as_view(), name="grid-product"),
]
