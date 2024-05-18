# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *
from products.models import Offer
from quickcart import constants


class ProductView(View):
    def get(self, request):
        offers = Offer.objects.all()
        print(offers)
        return render(request, constants.HOME_HTML, {"offers": offers})
