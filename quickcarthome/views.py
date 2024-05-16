# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *


class Home(View):

    def get(self, request):
        return HttpResponse("Hello")
