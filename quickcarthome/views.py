# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from quickcart import constants
from products.models import Offer


class Home(TemplateView):
    template_name = "html/home.html"

    def get_context_data(self):
        offers = Offer.objects.all()
        params = {"offers": offers}
        return params
