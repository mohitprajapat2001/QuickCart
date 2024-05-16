# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views import View


class ProductView(View):
    def get(self, request):
        return HttpResponse("Products")
