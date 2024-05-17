# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.views.generic import *


class Home(TemplateView):
    template_name = "html/base.html"
